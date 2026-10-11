#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""参考实现管理：对答案 / 还原 / 清回骨架。

仓库约定
--------
- ``.solutions/`` 与 ``exercises/`` 同构，保存每道题的**参考实现**。
- ``exercises/`` 里的作答文件默认是**骨架**：只保留函数签名与文档，
  函数体统一是 ``raise NotImplementedError('TODO: 实现 xxx')``。
  这样打开文件不会「顺手看到答案」。

用法::

    python tools/reference.py list                    # 看每道题的作答状态
    python tools/reference.py show 01-fizzbuzz        # 看参考实现（不改动任何文件）
    python tools/reference.py restore 01-fizzbuzz     # 用参考实现覆盖自己的文件
    python tools/reference.py blank 01-fizzbuzz       # 把自己的文件清回骨架
    python tools/reference.py save 04-two-sum         # 把自己的实现归档成参考答案
    python tools/reference.py restore --all --force   # 全部还原（CI 用）

``restore`` / ``blank`` 会覆盖你已经写的内容，所以默认拒绝动
「已作答」的文件，需要显式加 ``--force``。

只依赖 Python 标准库。
"""

from __future__ import annotations

import argparse
import ast
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXERCISES = ROOT / "exercises"
REFS = ROOT / ".solutions" / "exercises"

SOURCE_SUFFIXES = (".py", ".mjs", ".js", ".cjs")
BLANK_MARKER = "TODO: 实现"

PY_HEADER = '''{title}

【你的作答区】把下面的函数体补全，然后在本目录跑：

    python -m unittest -v

- 题面：同目录的 README.md
- 对答案（不改动文件）：python tools/reference.py show {slug}
- 从零重来：python tools/reference.py blank {slug}
- 还原参考实现：python tools/reference.py restore {slug}
'''

_JS_FUNC = re.compile(
    r"\bexport\s+(?:default\s+)?(?:async\s+)?function\s+(\w+)\s*\(([^)]*)\)\s*\{"
)


# --------------------------------------------------------------------------- #
# 路径与查找
# --------------------------------------------------------------------------- #
def ref_files() -> list[Path]:
    """``.solutions/`` 下的所有作答文件（solution.py、*.mjs ...）。"""
    if not REFS.is_dir():
        return []
    return sorted(
        p for p in REFS.rglob("*") if p.is_file() and p.suffix in SOURCE_SUFFIXES
    )


def exercise_files() -> list[Path]:
    """``exercises/`` 下的作答文件（不含测试文件）。"""
    if not EXERCISES.is_dir():
        return []
    return sorted(
        p
        for p in EXERCISES.rglob("*")
        if p.is_file()
        and p.suffix in SOURCE_SUFFIXES
        and not p.name.startswith("test_")
    )


def rel_slug(ref: Path) -> str:
    """``01-python-basics/01-fizzbuzz``"""
    return ref.parent.relative_to(REFS).as_posix()


def target_of(ref: Path) -> Path:
    """参考实现对应的、位于 ``exercises/`` 的作答文件。"""
    return EXERCISES / ref.relative_to(REFS)


def is_blank(text: str) -> bool:
    return BLANK_MARKER in text


# --------------------------------------------------------------------------- #
# 骨架生成
# --------------------------------------------------------------------------- #
def first_doc_line(src: str) -> str:
    """取 Python 模块 docstring 的第一行，作为骨架标题。"""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return ""
    doc = ast.get_docstring(tree, clean=True)
    return doc.splitlines()[0].strip() if doc else ""


_TOP_STARTERS = ("def ", "class ", "async def ", "@", "if __name__")


def _tidy(src: str) -> str:
    """ast.unparse 输出的空行偏少，给顶层 def / class / if __name__ 补两个空行。"""
    out: list[str] = []
    for line in src.rstrip().split("\n"):
        if line and not line[0].isspace() and line.startswith(_TOP_STARTERS):
            while out and not out[-1].strip():
                out.pop()
            if out:
                out.extend(["", ""])
        out.append(line)
    return "\n".join(out)


def blank_python(src: str, slug: str, title: str) -> str:
    """把 Python 参考实现清成骨架：保留 import / 常量 / 签名 / 文档字符串。"""
    tree = ast.parse(src)

    header = PY_HEADER.format(title=title or slug, slug=slug)
    head = tree.body[0] if tree.body else None
    if (
        isinstance(head, ast.Expr)
        and isinstance(head.value, ast.Constant)
        and isinstance(head.value.value, str)
    ):
        head.value = ast.Constant(header)
    else:
        tree.body.insert(0, ast.Expr(value=ast.Constant(header)))

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            body: list[ast.stmt] = []
            doc = ast.get_docstring(node, clean=False)
            if doc is not None:
                body.append(ast.Expr(value=ast.Constant(doc)))
            body.append(
                ast.Raise(
                    exc=ast.Call(
                        func=ast.Name(id="NotImplementedError", ctx=ast.Load()),
                        args=[ast.Constant(f"{BLANK_MARKER} {node.name}")],
                        keywords=[],
                    ),
                    cause=None,
                )
            )
            node.body = body

    return "# -*- coding: utf-8 -*-\n" + _tidy(ast.unparse(tree)) + "\n"


def blank_js(src: str) -> str:
    """把 JS 参考实现清成骨架：保留 JSDoc，函数体换成 throw。"""
    out: list[str] = []
    pos = 0
    while True:
        m = _JS_FUNC.search(src, pos)
        if not m:
            out.append(src[pos:])
            return "".join(out)

        out.append(src[pos : m.end()])
        name = m.group(1)

        depth = 1
        i = m.end()
        while i < len(src) and depth:
            ch = src[i]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            i += 1

        if depth:  # 括号不平衡，放弃改写这一段，原样保留
            out.append(src[m.end() :])
            return "".join(out)

        out.append(f"\n  throw new Error('{BLANK_MARKER} {name}');\n}}")
        pos = i


def make_blank(ref: Path) -> str:
    src = ref.read_text(encoding="utf-8")
    if ref.suffix == ".py":
        return blank_python(src, ref.parent.name, first_doc_line(src))
    return blank_js(src)


# --------------------------------------------------------------------------- #
# 子命令
# --------------------------------------------------------------------------- #
def select(refs: list[Path], patterns: list[str], use_all: bool) -> list[Path]:
    if use_all:
        return refs
    if not patterns:
        print("请给出题目标识（例如 01-fizzbuzz），或加 --all。")
        return []
    hits = [
        r
        for r in refs
        if any(p in f"{rel_slug(r)}/{r.name}" for p in patterns)
    ]
    if not hits:
        print("没有匹配到练习：" + "、".join(patterns))
    return hits


def cmd_list(args: argparse.Namespace) -> int:
    refs = ref_files()
    if not refs:
        print(f"找不到参考实现目录：{REFS}")
        return 1

    rows = [(f"{rel_slug(r)}/{r.name}", r) for r in refs]
    width = max(len(name) for name, _ in rows)

    print(f"参考实现来自 {REFS.relative_to(ROOT).as_posix()}\n")
    for name, ref in rows:
        target = target_of(ref)
        if not target.exists():
            state = "缺少作答文件"
        elif is_blank(target.read_text(encoding="utf-8")):
            state = "骨架（未作答）"
        else:
            state = "已作答"
        print(f"  {name:<{width}}  {state}")

    done = sum(
        1
        for _, ref in rows
        if target_of(ref).exists()
        and not is_blank(target_of(ref).read_text(encoding="utf-8"))
    )
    print(f"\n进度：{done} / {len(rows)}")
    return 0


def cmd_show(args: argparse.Namespace) -> int:
    refs = select(ref_files(), args.patterns, args.all)
    if not refs:
        return 1
    for ref in refs:
        print("=" * 70)
        print(f"== 参考实现：{rel_slug(ref)}/{ref.name}")
        print("=" * 70)
        print(ref.read_text(encoding="utf-8").rstrip())
        print()
    return 0


def _write_all(
    refs: list[Path], force: bool, action: str, produce
) -> int:
    changed = skipped = 0
    for ref in refs:
        target = target_of(ref)
        if target.exists() and not is_blank(target.read_text(encoding="utf-8")) and not force:
            print(
                f"  跳过 {rel_slug(ref)}：这里已经有你写的内容，"
                f"确认要{action}请加 --force"
            )
            skipped += 1
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(produce(ref), encoding="utf-8", newline="\n")
        print(f"  已{action} {rel_slug(ref)}/{ref.name}")
        changed += 1

    print(f"\n共{action} {changed} 个文件" + (f"，跳过 {skipped} 个" if skipped else ""))
    return 0


def cmd_restore(args: argparse.Namespace) -> int:
    refs = select(ref_files(), args.patterns, args.all)
    if not refs:
        return 1
    return _write_all(
        refs, args.force, "还原", lambda ref: ref.read_text(encoding="utf-8")
    )


def cmd_blank(args: argparse.Namespace) -> int:
    refs = select(ref_files(), args.patterns, args.all)
    if not refs:
        return 1
    return _write_all(refs, args.force, "清回骨架", make_blank)


def cmd_save(args: argparse.Namespace) -> int:
    """把自己在 exercises/ 里的实现归档成该题的参考答案。"""
    posts = [
        p
        for p in exercise_files()
        if any(
            pat in f"{p.parent.relative_to(EXERCISES).as_posix()}/{p.name}"
            for pat in args.patterns
        )
    ]
    if not posts:
        print("在 exercises/ 里没找到匹配的作答文件：" + "、".join(args.patterns))
        return 1

    for post in posts:
        rel = post.relative_to(EXERCISES)
        ref = REFS / rel
        ref.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(post, ref)
        print(f"  已归档 {rel.as_posix()}")
        if not args.keep:
            post.write_text(make_blank(ref), encoding="utf-8", newline="\n")
            print(f"  已清成骨架 {rel.as_posix()}")

    if not args.keep:
        print("\n想拿回答案：python tools/reference.py restore <题号>")
    return 0


# --------------------------------------------------------------------------- #
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="参考实现管理：对答案 / 还原 / 清回骨架",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("用法::")[-1].strip(),
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("list", help="列出所有练习与作答状态")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("show", help="打印参考实现（不改动文件）")
    p.add_argument("patterns", nargs="*", help="题目标识，如 01-fizzbuzz")
    p.add_argument("--all", action="store_true", help="作用于全部练习")
    p.set_defaults(func=cmd_show)

    p = sub.add_parser("restore", help="用参考实现覆盖作答文件")
    p.add_argument("patterns", nargs="*", help="题目标识，如 01-fizzbuzz")
    p.add_argument("--all", action="store_true", help="作用于全部练习")
    p.add_argument("--force", action="store_true", help="允许覆盖已作答的文件")
    p.set_defaults(func=cmd_restore)

    p = sub.add_parser("blank", help="把作答文件清回骨架")
    p.add_argument("patterns", nargs="*", help="题目标识，如 01-fizzbuzz")
    p.add_argument("--all", action="store_true", help="作用于全部练习")
    p.add_argument("--force", action="store_true", help="允许覆盖已作答的文件")
    p.set_defaults(func=cmd_blank)

    p = sub.add_parser("save", help="把作答文件归档成参考答案（默认同时清成骨架）")
    p.add_argument("patterns", nargs="+", help="练习路径或题号，如 04-two-sum")
    p.add_argument("--keep", action="store_true", help="只归档，不把原文件清成骨架")
    p.set_defaults(func=cmd_save)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not REFS.is_dir():
        print(f"找不到参考实现目录：{REFS}")
        print("（该目录由仓库提供，缺失时请先 git pull）")
        return 1
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一键运行 code-practice 仓库内全部练习的测试。

用法::

    python tools/run_all_tests.py                # 跑全部
    python tools/run_all_tests.py 01             # 只跑路径里含 "01" 的练习
    python tools/run_all_tests.py 04-discrete    # 只跑离散数学赛道
    python tools/run_all_tests.py -v             # 详细输出（透传给 unittest）
    python tools/run_all_tests.py --list         # 只列出找到的练习，不执行

设计要点：每个练习目录单独开一个子进程跑测试。因为所有测试文件都叫
``test_solution.py``，在同一个进程里导入会互相覆盖模块名，开子进程最省心。
整个脚本只依赖 Python 标准库。
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXERCISES = ROOT / "exercises"

PY_TEST_GLOB = "test_*.py"
JS_TEST_GLOBS = ("*.test.js", "*.test.mjs", "*.test.cjs")

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
DIM = "\033[2m"
RESET = "\033[0m"


def colorize(text: str, color: str) -> str:
    """Windows 终端不一定支持 ANSI，简单判断一下。"""
    if sys.platform == "win32" and not sys.stdout.isatty():
        return text
    return f"{color}{text}{RESET}"


def find_exercises(filters: list[str]) -> list[tuple[str, Path, bool, bool]]:
    """返回 [(相对路径, 目录, 有Python测试, 有JS测试)]。"""
    found: list[tuple[str, Path, bool, bool]] = []
    if not EXERCISES.is_dir():
        return found
    for track in sorted(p for p in EXERCISES.iterdir() if p.is_dir()):
        for ex in sorted(p for p in track.iterdir() if p.is_dir()):
            rel = f"{track.name}/{ex.name}"
            if filters and not any(f in rel for f in filters):
                continue
            has_py = any(ex.glob(PY_TEST_GLOB))
            has_js = any(any(ex.glob(g)) for g in JS_TEST_GLOBS)
            if has_py or has_js:
                found.append((rel, ex, has_py, has_js))
    return found


def run_python(ex_dir: Path, extra: list[str]) -> int:
    cmd = [
        sys.executable,
        "-m",
        "unittest",
        "discover",
        "-s",
        ".",
        "-p",
        PY_TEST_GLOB,
        *extra,
    ]
    proc = subprocess.run(cmd, cwd=ex_dir, text=True, encoding="utf-8", errors="replace")
    return proc.returncode


def run_node(ex_dir: Path) -> int:
    node = shutil.which("node")
    if not node:
        print(colorize("  ! 未找到 node，跳过 JS 测试", YELLOW))
        return 0
    cmd = [node, "--test"]
    proc = subprocess.run(cmd, cwd=ex_dir, text=True, encoding="utf-8", errors="replace")
    return proc.returncode


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="跑遍仓库里所有练习的测试")
    parser.add_argument("filters", nargs="*", help="按路径片段过滤，例如 01 / 04-discrete")
    parser.add_argument("-v", "--verbose", action="store_true", help="详细输出")
    parser.add_argument("--list", action="store_true", help="只列出练习，不执行")
    args = parser.parse_args(argv)

    exercises = find_exercises(args.filters)

    if not exercises:
        print("没有找到任何带测试的练习。")
        return 0

    if args.list:
        for rel, _ex, has_py, has_js in exercises:
            kinds = "+".join(k for k, ok in (("py", has_py), ("js", has_js)) if ok)
            print(f"{rel}  [{kinds}]")
        return 0

    extra = ["-v"] if args.verbose else []
    results: list[tuple[str, bool]] = []

    for rel, ex_dir, has_py, has_js in exercises:
        print()
        print("=" * 68)
        print(f">> {rel}")
        print("=" * 68)
        ok = True
        if has_py:
            ok = run_python(ex_dir, extra) == 0 and ok
        if has_js:
            ok = run_node(ex_dir) == 0 and ok
        results.append((rel, ok))

    passed = [r for r, ok in results if ok]
    failed = [r for r, ok in results if not ok]

    print()
    print("=" * 68)
    print(f"汇总：共 {len(results)} 道练习 —— "
          f"{colorize(f'通过 {len(passed)}', GREEN)} / "
          f"{colorize(f'未通过 {len(failed)}', RED if failed else DIM)}")
    print("=" * 68)
    for rel, ok in results:
        mark = colorize("PASS", GREEN) if ok else colorize("FAIL", RED)
        print(f"  [{mark}] {rel}")

    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())

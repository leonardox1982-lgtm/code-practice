#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成一道新练习的骨架。

用法::

    python tools/new_exercise.py 03-algorithms 04-two-sum
    python tools/new_exercise.py 03-algorithms 04-two-sum --title "两数之和"

会创建::

    exercises/03-algorithms/04-two-sum/
    ├── README.md          题面骨架，待你补全
    ├── solution.py        参考实现骨架
    └── test_solution.py   测试骨架

只依赖 Python 标准库。
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXERCISES = ROOT / "exercises"

README_TMPL = """# {num} · {title}

**赛道**：{track}
**考点**：（待补：这道题练什么）

## 题目

（待补：把题目写清楚，包含输入输出的约定、边界情况。）

## 示例

```python
# （待补）
```

## 提示

- （待补）

## 验收标准

- [ ] `python -m unittest -v` 全部通过
- [ ] （待补：额外的要求，例如「不许用内置 sorted」）

## 参考

（可选：来源链接、相关章节。）
"""

SOLUTION_TMPL = '''# -*- coding: utf-8 -*-
"""{num} · {title}

自己先写一版，然后把这里替换掉。
卡住了就 `git checkout -- {rel_path}/solution.py` 回到参考实现。
"""


def {func}({params}){ret}:
    """（待补：函数说明）"""
    raise NotImplementedError("TODO: 实现 {func}")


if __name__ == "__main__":
    # 手动试一下
    print({func}({call_args}))
'''

TEST_TMPL = '''# -*- coding: utf-8 -*-
"""{num} · {title} —— 单元测试。

跑测试：在本目录下执行 `python -m unittest -v`
"""

import unittest

from solution import {func}


class Test{cls}(unittest.TestCase):
    def test_todo(self):
        self.skipTest("待补：把这里的用例换成真正的断言")
        # self.assertEqual({func}(...), ...)


if __name__ == "__main__":
    unittest.main(verbosity=2)
'''


def to_func_name(slug: str) -> str:
    """'04-two-sum' -> 'two_sum'"""
    name = re.sub(r"^\d+[-_]", "", slug)
    name = re.sub(r"[^0-9A-Za-z]+", "_", name).strip("_").lower()
    return name or "solve"


def to_class_name(slug: str) -> str:
    return "".join(part.capitalize() for part in to_func_name(slug).split("_"))


def main() -> int:
    parser = argparse.ArgumentParser(description="生成一道新练习的骨架")
    parser.add_argument("track", help="赛道目录名，例如 03-algorithms")
    parser.add_argument("slug", help="练习目录名，例如 04-two-sum")
    parser.add_argument("--title", default=None, help="中文标题，默认用 slug")
    args = parser.parse_args()

    track_dir = EXERCISES / args.track
    if not track_dir.is_dir():
        existing = sorted(p.name for p in EXERCISES.iterdir() if p.is_dir())
        print(f"赛道不存在：{args.track}")
        print("现有赛道：" + "、".join(existing))
        return 1

    ex_dir = track_dir / args.slug
    if ex_dir.exists():
        print(f"目录已存在，未做改动：{ex_dir}")
        return 1

    num = args.slug.split("-")[0] if args.slug[0].isdigit() else args.slug
    title = args.title or to_func_name(args.slug)
    func = to_func_name(args.slug)
    cls = to_class_name(args.slug)
    rel_path = f"exercises/{args.track}/{args.slug}"

    ex_dir.mkdir(parents=True)

    (ex_dir / "README.md").write_text(
        README_TMPL.format(num=num, title=title, track=args.track), encoding="utf-8"
    )
    (ex_dir / "solution.py").write_text(
        SOLUTION_TMPL.format(
            num=num,
            title=title,
            func=func,
            params="",
            ret="",
            call_args="",
            rel_path=rel_path,
        ),
        encoding="utf-8",
    )
    (ex_dir / "test_solution.py").write_text(
        TEST_TMPL.format(num=num, title=title, func=func, cls=cls), encoding="utf-8"
    )

    print(f"已创建练习骨架：{ex_dir}")
    print("  待补：README.md 题面、solution.py 实现、test_solution.py 断言")
    print(f"  跑测试：cd {rel_path} && python -m unittest -v")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

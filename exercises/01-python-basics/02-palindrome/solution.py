# -*- coding: utf-8 -*-
"""02 · 回文判断

自己先写一版，然后把这里替换掉。
卡住了就 `git checkout -- exercises/01-python-basics/02-palindrome/solution.py` 回到参考实现。
"""


def normalize(text: str) -> str:
    """只保留字母与数字，并统一转小写。"""
    return "".join(ch.lower() for ch in text if ch.isalnum())


def is_palindrome(text: str) -> bool:
    """忽略大小写、空格与标点，判断是否为回文。"""
    cleaned = normalize(text)
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    samples = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "上海自来水来自海上",
        "",
        "0P",
    ]
    for s in samples:
        print(f"{is_palindrome(s)!s:>5}  {s!r}")

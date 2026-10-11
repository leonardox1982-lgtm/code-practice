# -*- coding: utf-8 -*-
"""03 · 词频统计

自己先写一版，然后把这里替换掉。
卡住了就 `git checkout -- exercises/01-python-basics/03-word-count/solution.py` 回到参考实现。
"""

import re
from collections import Counter

WORD_RE = re.compile(r"[A-Za-z][A-Za-z']*")


def word_count(text: str) -> dict[str, int]:
    """统计英文单词词频（忽略大小写）。"""
    words = WORD_RE.findall(text)
    return dict(Counter(w.lower() for w in words))


def top_n(text: str, n: int = 3) -> list[tuple[str, int]]:
    """返回词频前 n 名，次数相同时按单词升序。"""
    if n <= 0:
        return []
    counts = word_count(text)
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:n]


if __name__ == "__main__":
    sample = """
    It was the best of times, it was the worst of times,
    it was the age of wisdom, it was the age of foolishness.
    """
    print(word_count(sample))
    print(top_n(sample, 5))

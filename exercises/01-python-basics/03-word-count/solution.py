# -*- coding: utf-8 -*-
"""03 · 词频统计

【你的作答区】把下面的函数体补全，然后在本目录跑：

    python -m unittest -v

- 题面：同目录的 README.md
- 对答案（不改动文件）：python tools/reference.py show 03-word-count
- 从零重来：python tools/reference.py blank 03-word-count
- 还原参考实现：python tools/reference.py restore 03-word-count
"""
import re
from collections import Counter
WORD_RE = re.compile("[A-Za-z][A-Za-z']*")


def word_count(text: str) -> dict[str, int]:
    """统计英文单词词频（忽略大小写）。"""
    raise NotImplementedError('TODO: 实现 word_count')


def top_n(text: str, n: int=3) -> list[tuple[str, int]]:
    """返回词频前 n 名，次数相同时按单词升序。"""
    raise NotImplementedError('TODO: 实现 top_n')


if __name__ == '__main__':
    sample = '\n    It was the best of times, it was the worst of times,\n    it was the age of wisdom, it was the age of foolishness.\n    '
    print(word_count(sample))
    print(top_n(sample, 5))

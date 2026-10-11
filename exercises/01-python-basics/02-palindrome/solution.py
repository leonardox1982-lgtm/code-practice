# -*- coding: utf-8 -*-
"""02 · 回文判断

【你的作答区】把下面的函数体补全，然后在本目录跑：

    python -m unittest -v

- 题面：同目录的 README.md
- 对答案（不改动文件）：python tools/reference.py show 02-palindrome
- 从零重来：python tools/reference.py blank 02-palindrome
- 还原参考实现：python tools/reference.py restore 02-palindrome
"""


def normalize(text: str) -> str:
    """只保留字母与数字，并统一转小写。"""
    raise NotImplementedError('TODO: 实现 normalize')


def is_palindrome(text: str) -> bool:
    """忽略大小写、空格与标点，判断是否为回文。"""
    raise NotImplementedError('TODO: 实现 is_palindrome')


if __name__ == '__main__':
    samples = ['A man, a plan, a canal: Panama', 'race a car', '上海自来水来自海上', '', '0P']
    for s in samples:
        print(f'{is_palindrome(s)!s:>5}  {s!r}')

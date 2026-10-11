# -*- coding: utf-8 -*-
"""01 · FizzBuzz

【你的作答区】把下面的函数体补全，然后在本目录跑：

    python -m unittest -v

- 题面：同目录的 README.md
- 对答案（不改动文件）：python tools/reference.py show 01-fizzbuzz
- 从零重来：python tools/reference.py blank 01-fizzbuzz
- 还原参考实现：python tools/reference.py restore 01-fizzbuzz
"""


def fizzbuzz(n: int) -> str:
    """按 FizzBuzz 规则返回 n 对应的字符串。"""
    raise NotImplementedError('TODO: 实现 fizzbuzz')


def fizzbuzz_list(n: int) -> list[str]:
    """返回 1..n 的 FizzBuzz 序列，n <= 0 时返回空列表。"""
    raise NotImplementedError('TODO: 实现 fizzbuzz_list')


if __name__ == '__main__':
    print(' '.join(fizzbuzz_list(20)))

# -*- coding: utf-8 -*-
"""01 · 素数筛与质因数分解

【你的作答区】把下面的函数体补全，然后在本目录跑：

    python -m unittest -v

- 题面：同目录的 README.md
- 对答案（不改动文件）：python tools/reference.py show 01-sieve-prime
- 从零重来：python tools/reference.py blank 01-sieve-prime
- 还原参考实现：python tools/reference.py restore 01-sieve-prime
"""


def sieve(limit: int) -> list[int]:
    """返回 [2, limit] 内的全部素数。O(n log log n)。"""
    raise NotImplementedError('TODO: 实现 sieve')


def is_prime(n: int) -> bool:
    """试除判素，做到 sqrt(n)；用 6k±1 轮子跳过明显的合数。"""
    raise NotImplementedError('TODO: 实现 is_prime')


def prime_factors(n: int) -> list[int]:
    """n 的质因数（带重数），升序；n < 2 返回 []。"""
    raise NotImplementedError('TODO: 实现 prime_factors')


def count_primes(limit: int) -> int:
    """π(limit)：不超过 limit 的素数个数。"""
    raise NotImplementedError('TODO: 实现 count_primes')


if __name__ == '__main__':
    print('30 以内素数:', sieve(30))
    print('97 是素数吗:', is_prime(97), '| 91 是素数吗:', is_prime(91))
    print('360 的质因数:', prime_factors(360))
    print('π(1_000_000) =', count_primes(1000000))

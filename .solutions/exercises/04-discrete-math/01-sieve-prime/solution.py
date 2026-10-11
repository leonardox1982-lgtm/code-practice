# -*- coding: utf-8 -*-
"""01 · 素数筛与质因数分解

自己先写一版，然后把这里替换掉。
卡住了就 `git checkout -- exercises/04-discrete-math/01-sieve-prime/solution.py` 回到参考实现。
"""


def sieve(limit: int) -> list[int]:
    """返回 [2, limit] 内的全部素数。O(n log log n)。"""
    if limit < 2:
        return []
    flags = bytearray([1]) * (limit + 1)
    flags[0] = flags[1] = 0
    for p in range(2, int(limit ** 0.5) + 1):
        if flags[p]:
            flags[p * p::p] = b"\x00" * len(flags[p * p::p])
    return [i for i in range(2, limit + 1) if flags[i]]


def is_prime(n: int) -> bool:
    """试除判素，做到 sqrt(n)；用 6k±1 轮子跳过明显的合数。"""
    if n < 2:
        return False
    if n < 4:
        return True                      # 2, 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def prime_factors(n: int) -> list[int]:
    """n 的质因数（带重数），升序；n < 2 返回 []。"""
    if n < 0:
        raise ValueError("n must be non-negative")
    factors: list[int] = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1 if d == 2 else 2          # 2 之后只试奇数
    if n > 1:
        factors.append(n)
    return factors


def count_primes(limit: int) -> int:
    """π(limit)：不超过 limit 的素数个数。"""
    return len(sieve(limit))


if __name__ == "__main__":
    print("30 以内素数:", sieve(30))
    print("97 是素数吗:", is_prime(97), "| 91 是素数吗:", is_prime(91))
    print("360 的质因数:", prime_factors(360))
    print("π(1_000_000) =", count_primes(1_000_000))

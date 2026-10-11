# -*- coding: utf-8 -*-
"""02 · 斐波那契的三种写法

自己先写一版，然后把这里替换掉。
卡住了就 `git checkout -- exercises/03-algorithms/02-fib-memo/solution.py` 回到参考实现。
"""

from functools import lru_cache

_recursive_calls = 0  # 仅用于教学：统计朴素递归的调用次数


def fib_recursive(n: int) -> int:
    """朴素递归，指数级复杂度，n 大了千万别用。"""
    global _recursive_calls
    _recursive_calls += 1
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def recursive_call_count(n: int) -> int:
    """返回朴素递归算 fib(n) 需要多少次函数调用。"""
    global _recursive_calls
    _recursive_calls = 0
    fib_recursive(n)
    return _recursive_calls


@lru_cache(maxsize=None)
def _fib_cached(n: int) -> int:
    if n < 2:
        return n
    return _fib_cached(n - 1) + _fib_cached(n - 2)


def fib_memo(n: int) -> int:
    """记忆化递归，O(n)。"""
    if n < 0:
        raise ValueError("n must be non-negative")
    return _fib_cached(n)


def fib_iter(n: int) -> int:
    """迭代，O(n) 时间、O(1) 空间。"""
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_list(n: int) -> list[int]:
    """返回前 n 项 [F(0), F(1), ..., F(n-1)]。"""
    if n <= 0:
        return []
    out = [0, 1]
    while len(out) < n:
        out.append(out[-1] + out[-2])
    return out[:n]


if __name__ == "__main__":
    print("前 10 项        :", fib_list(10))
    print("fib_memo(100)   :", fib_memo(100))
    print("fib_iter(100)   :", fib_iter(100))
    print("fib_iter(1000) 位数:", len(str(fib_iter(1000))))
    for n in (5, 10, 20, 25):
        print(f"朴素递归 fib({n}) 的调用次数: {recursive_call_count(n)}")

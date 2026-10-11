# -*- coding: utf-8 -*-
"""02 · 斐波那契的三种写法

【你的作答区】把下面的函数体补全，然后在本目录跑：

    python -m unittest -v

- 题面：同目录的 README.md
- 对答案（不改动文件）：python tools/reference.py show 02-fib-memo
- 从零重来：python tools/reference.py blank 02-fib-memo
- 还原参考实现：python tools/reference.py restore 02-fib-memo
"""
from functools import lru_cache
_recursive_calls = 0


def fib_recursive(n: int) -> int:
    """朴素递归，指数级复杂度，n 大了千万别用。"""
    raise NotImplementedError('TODO: 实现 fib_recursive')


def recursive_call_count(n: int) -> int:
    """返回朴素递归算 fib(n) 需要多少次函数调用。"""
    raise NotImplementedError('TODO: 实现 recursive_call_count')


@lru_cache(maxsize=None)


def _fib_cached(n: int) -> int:
    raise NotImplementedError('TODO: 实现 _fib_cached')


def fib_memo(n: int) -> int:
    """记忆化递归，O(n)。"""
    raise NotImplementedError('TODO: 实现 fib_memo')


def fib_iter(n: int) -> int:
    """迭代，O(n) 时间、O(1) 空间。"""
    raise NotImplementedError('TODO: 实现 fib_iter')


def fib_list(n: int) -> list[int]:
    """返回前 n 项 [F(0), F(1), ..., F(n-1)]。"""
    raise NotImplementedError('TODO: 实现 fib_list')


if __name__ == '__main__':
    print('前 10 项        :', fib_list(10))
    print('fib_memo(100)   :', fib_memo(100))
    print('fib_iter(100)   :', fib_iter(100))
    print('fib_iter(1000) 位数:', len(str(fib_iter(1000))))
    for n in (5, 10, 20, 25):
        print(f'朴素递归 fib({n}) 的调用次数: {recursive_call_count(n)}')

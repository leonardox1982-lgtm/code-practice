# -*- coding: utf-8 -*-
"""02 · 斐波那契的三种写法 —— 单元测试。

跑测试：在本目录下执行 `python -m unittest -v`
"""

import unittest

from solution import (
    fib_iter,
    fib_list,
    fib_memo,
    fib_recursive,
    recursive_call_count,
)

SMALL = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]


class TestSmallValues(unittest.TestCase):
    def test_recursive(self):
        for n, expected in enumerate(SMALL):
            with self.subTest(n=n):
                self.assertEqual(fib_recursive(n), expected)

    def test_memo(self):
        for n, expected in enumerate(SMALL):
            with self.subTest(n=n):
                self.assertEqual(fib_memo(n), expected)

    def test_iter(self):
        for n, expected in enumerate(SMALL):
            with self.subTest(n=n):
                self.assertEqual(fib_iter(n), expected)


class TestBigValues(unittest.TestCase):
    def test_memo_100(self):
        self.assertEqual(fib_memo(100), 354224848179261915075)

    def test_iter_100(self):
        self.assertEqual(fib_iter(100), 354224848179261915075)

    def test_agreement(self):
        for n in (50, 100, 200, 300):
            with self.subTest(n=n):
                self.assertEqual(fib_memo(n), fib_iter(n))

    def test_iter_1000_has_209_digits(self):
        self.assertEqual(len(str(fib_iter(1000))), 209)

    def test_recurrence_relation(self):
        for n in (10, 40, 77):
            with self.subTest(n=n):
                self.assertEqual(fib_iter(n), fib_iter(n - 1) + fib_iter(n - 2))


class TestFibList(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(fib_list(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_degenerate(self):
        self.assertEqual(fib_list(0), [])
        self.assertEqual(fib_list(-3), [])

    def test_one_and_two(self):
        self.assertEqual(fib_list(1), [0])
        self.assertEqual(fib_list(2), [0, 1])

    def test_consistent_with_iter(self):
        values = fib_list(30)
        self.assertEqual([fib_iter(i) for i in range(30)], values)


class TestErrors(unittest.TestCase):
    def test_negative_raises(self):
        for fn in (fib_recursive, fib_memo, fib_iter):
            with self.subTest(fn=fn.__name__):
                with self.assertRaises(ValueError):
                    fn(-1)


class TestRecursiveIsExponential(unittest.TestCase):
    """用调用次数证明朴素递归是指数级的 —— 这就是要记忆化的理由。"""

    def test_call_count_grows_like_fibonacci(self):
        counts = [recursive_call_count(n) for n in (1, 5, 10, 15, 20)]
        self.assertEqual(counts, sorted(counts))
        # 每加 5，调用次数大约乘 5.5 倍（≈φ^5）
        for prev, cur in zip(counts, counts[1:]):
            self.assertGreater(cur / prev, 3.0)

    def test_call_count_is_itself_fibonacci_like(self):
        # F(n) 的调用次数约为 2*F(n+1) - 1
        for n in (5, 10, 15, 18):
            with self.subTest(n=n):
                self.assertEqual(recursive_call_count(n), 2 * fib_iter(n + 1) - 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)

# -*- coding: utf-8 -*-
"""03 · 最大子数组和 —— 单元测试。

跑测试：在本目录下执行 `python -m unittest -v`
"""

import random
import unittest

from solution import max_subarray, max_subarray_bruteforce, max_subarray_range


class TestMaxSubarray(unittest.TestCase):
    def test_classic(self):
        self.assertEqual(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_single(self):
        self.assertEqual(max_subarray([5]), 5)
        self.assertEqual(max_subarray([-5]), -5)

    def test_all_positive(self):
        self.assertEqual(max_subarray([1, 2, 3, 4]), 10)

    def test_all_negative(self):
        self.assertEqual(max_subarray([-3, -1, -2]), -1)
        self.assertEqual(max_subarray([-8, -3, -5, -4]), -3)

    def test_zeros(self):
        self.assertEqual(max_subarray([0, 0, 0]), 0)
        self.assertEqual(max_subarray([-1, 0, -1]), 0)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            max_subarray([])


class TestMaxSubarrayRange(unittest.TestCase):
    def test_classic(self):
        self.assertEqual(max_subarray_range([-2, 1, -3, 4, -1, 2, 1, -5, 4]), (6, 3, 7))

    def test_single(self):
        self.assertEqual(max_subarray_range([5]), (5, 0, 1))

    def test_all_negative_picks_largest(self):
        self.assertEqual(max_subarray_range([-3, -1, -2]), (-1, 1, 2))

    def test_tie_prefers_earliest(self):
        # 最大值 2 在下标 0 和下标 2 都能取到，应该选更靠前的 [0, 1)
        self.assertEqual(max_subarray_range([2, -5, 2]), (2, 0, 1))

    def test_full_array(self):
        self.assertEqual(max_subarray_range([1, 2, 3]), (6, 0, 3))

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            max_subarray_range([])


class TestRangeConsistency(unittest.TestCase):
    def test_slice_sum_equals_max(self):
        cases = [
            [-2, 1, -3, 4, -1, 2, 1, -5, 4],
            [1, -1, 1, -1],
            [-5],
            [0, -1, 0, 0],
            [3, -2, 5, -1, 2],
        ]
        for data in cases:
            with self.subTest(data=data):
                total, start, end = max_subarray_range(data)
                self.assertEqual(sum(data[start:end]), total)
                self.assertEqual(total, max_subarray(data))
                self.assertLess(start, end)


class TestAgainstBruteforce(unittest.TestCase):
    def test_random_arrays(self):
        rng = random.Random(20261011)
        for _ in range(400):
            data = [rng.randrange(-9, 10) for _ in range(rng.randrange(1, 25))]
            with self.subTest(data=data):
                expected = max_subarray_bruteforce(data)
                self.assertEqual(max_subarray(data), expected)
                total, start, end = max_subarray_range(data)
                self.assertEqual(total, expected)
                self.assertEqual(sum(data[start:end]), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)

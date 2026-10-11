# -*- coding: utf-8 -*-
"""03 · 二分查找与边界 —— 单元测试。

跑测试：在本目录下执行 `python -m unittest -v`
"""

import random
import unittest

from solution import binary_search, count_occurrences, lower_bound, upper_bound


class TestLowerUpperBound(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(lower_bound([], 1), 0)
        self.assertEqual(upper_bound([], 1), 0)

    def test_no_match_below_range(self):
        nums = [10, 20, 30]
        self.assertEqual(lower_bound(nums, 5), 0)
        self.assertEqual(upper_bound(nums, 5), 0)

    def test_no_match_above_range(self):
        nums = [10, 20, 30]
        self.assertEqual(lower_bound(nums, 99), 3)
        self.assertEqual(upper_bound(nums, 99), 3)

    def test_duplicates(self):
        nums = [1, 2, 2, 2, 3, 5]
        self.assertEqual(lower_bound(nums, 2), 1)
        self.assertEqual(upper_bound(nums, 2), 4)
        self.assertEqual(count_occurrences(nums, 2), 3)

    def test_all_equal(self):
        nums = [7, 7, 7, 7]
        self.assertEqual(lower_bound(nums, 7), 0)
        self.assertEqual(upper_bound(nums, 7), 4)
        self.assertEqual(count_occurrences(nums, 7), 4)

    def test_single_element(self):
        self.assertEqual(lower_bound([5], 5), 0)
        self.assertEqual(upper_bound([5], 5), 1)
        self.assertEqual(lower_bound([5], 4), 0)
        self.assertEqual(upper_bound([5], 6), 1)

    def test_boundary_exact(self):
        nums = [1, 3, 5, 7]
        self.assertEqual(lower_bound(nums, 1), 0)
        self.assertEqual(upper_bound(nums, 1), 1)
        self.assertEqual(lower_bound(nums, 7), 3)
        self.assertEqual(upper_bound(nums, 7), 4)


class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        nums = [1, 2, 3, 5, 8, 13, 21]
        for i, v in enumerate(nums):
            with self.subTest(v=v):
                self.assertEqual(nums[binary_search(nums, v)], v)

    def test_not_found(self):
        nums = [1, 2, 3, 5, 8, 13, 21]
        for v in (0, 4, 6, 100):
            with self.subTest(v=v):
                self.assertEqual(binary_search(nums, v), -1)

    def test_empty(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_single(self):
        self.assertEqual(binary_search([9], 9), 0)
        self.assertEqual(binary_search([9], 10), -1)

    def test_with_duplicates_returns_valid_index(self):
        nums = [1, 2, 2, 2, 3]
        idx = binary_search(nums, 2)
        self.assertIn(idx, (1, 2, 3))
        self.assertEqual(nums[idx], 2)


class TestAgainstBruteForce(unittest.TestCase):
    """随机对拍：二分的答案必须和暴力解法一致。"""

    def test_random_arrays(self):
        rng = random.Random(20261011)
        for _ in range(300):
            nums = sorted(rng.randrange(0, 12) for _ in range(rng.randrange(0, 30)))
            target = rng.randrange(-1, 13)

            expected_lower = next((i for i, v in enumerate(nums) if v >= target), len(nums))
            expected_upper = next((i for i, v in enumerate(nums) if v > target), len(nums))

            self.assertEqual(lower_bound(nums, target), expected_lower)
            self.assertEqual(upper_bound(nums, target), expected_upper)
            self.assertEqual(
                count_occurrences(nums, target),
                sum(1 for v in nums if v == target),
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)

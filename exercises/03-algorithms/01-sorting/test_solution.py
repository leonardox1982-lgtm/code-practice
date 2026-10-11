# -*- coding: utf-8 -*-
"""01 · 排序（分治）—— 单元测试。

跑测试：在本目录下执行 `python -m unittest -v`
"""

import random
import unittest

from solution import merge, merge_sort, quick_sort


class TestMerge(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(merge([1, 3, 5], [2, 4]), [1, 2, 3, 4, 5])

    def test_empty_sides(self):
        self.assertEqual(merge([], [1, 2]), [1, 2])
        self.assertEqual(merge([1, 2], []), [1, 2])
        self.assertEqual(merge([], []), [])

    def test_stability_prefers_left(self):
        # 值相等时先取左边：用 (值, 来源) 元组来验证
        left = [(1, "L"), (2, "L")]
        right = [(1, "R"), (2, "R")]
        self.assertEqual(merge(left, right), [(1, "L"), (1, "R"), (2, "L"), (2, "R")])


class TestSorts(unittest.TestCase):
    SORTS = (("quick_sort", quick_sort), ("merge_sort", merge_sort))

    def test_degenerate_inputs(self):
        for name, fn in self.SORTS:
            with self.subTest(sort=name):
                self.assertEqual(fn([]), [])
                self.assertEqual(fn([1]), [1])
                self.assertEqual(fn([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_simple(self):
        for name, fn in self.SORTS:
            with self.subTest(sort=name):
                self.assertEqual(fn([3, 1, 2]), [1, 2, 3])
                self.assertEqual(fn([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
                self.assertEqual(fn([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_negatives_and_duplicates(self):
        data = [0, -1, 3, -1, 2, 0, 0, -5]
        expected = sorted(data)
        for name, fn in self.SORTS:
            with self.subTest(sort=name):
                self.assertEqual(fn(data), expected)

    def test_does_not_mutate_input(self):
        data = [3, 1, 2]
        snapshot = list(data)
        quick_sort(data)
        merge_sort(data)
        self.assertEqual(data, snapshot)

    def test_random_against_builtin(self):
        rng = random.Random(20261011)
        for _ in range(120):
            data = [rng.randrange(-50, 50) for _ in range(rng.randrange(0, 60))]
            expected = sorted(data)
            for name, fn in self.SORTS:
                with self.subTest(sort=name, n=len(data)):
                    self.assertEqual(fn(data), expected)

    def test_many_duplicates_does_not_blow_up(self):
        data = [7] * 5000 + [3] * 5000
        self.assertEqual(quick_sort(data), sorted(data))
        self.assertEqual(merge_sort(data), sorted(data))

    def test_strings(self):
        self.assertEqual(quick_sort(["pear", "apple", "fig"]), ["apple", "fig", "pear"])
        self.assertEqual(merge_sort(["pear", "apple", "fig"]), ["apple", "fig", "pear"])


if __name__ == "__main__":
    unittest.main(verbosity=2)

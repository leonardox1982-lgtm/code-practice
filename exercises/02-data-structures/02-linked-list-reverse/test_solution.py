# -*- coding: utf-8 -*-
"""02 · 单链表反转 —— 单元测试。

跑测试：在本目录下执行 `python -m unittest -v`
"""

import unittest

from solution import Node, build, reverse, reverse_recursive, to_list


class TestBuildAndToList(unittest.TestCase):
    def test_roundtrip(self):
        self.assertEqual(to_list(build([1, 2, 3])), [1, 2, 3])

    def test_empty(self):
        self.assertIsNone(build([]))
        self.assertEqual(to_list(None), [])

    def test_single(self):
        head = build([42])
        self.assertIsInstance(head, Node)
        self.assertEqual(head.value, 42)
        self.assertIsNone(head.next)
        self.assertEqual(to_list(head), [42])

    def test_chain_links(self):
        head = build([1, 2, 3])
        self.assertEqual(head.next.value, 2)
        self.assertEqual(head.next.next.value, 3)
        self.assertIsNone(head.next.next.next)

    def test_cycle_is_detected(self):
        a, b = Node(1), Node(2)
        a.next = b
        b.next = a
        with self.assertRaises(ValueError):
            to_list(a)


class TestReverse(unittest.TestCase):
    def test_degenerate(self):
        self.assertIsNone(reverse(None))
        self.assertEqual(to_list(reverse(build([1]))), [1])

    def test_two_nodes(self):
        self.assertEqual(to_list(reverse(build([1, 2]))), [2, 1])

    def test_even_length(self):
        self.assertEqual(to_list(reverse(build([1, 2, 3, 4]))), [4, 3, 2, 1])

    def test_odd_length(self):
        self.assertEqual(to_list(reverse(build([1, 2, 3, 4, 5]))), [5, 4, 3, 2, 1])

    def test_long_list(self):
        values = list(range(100))
        self.assertEqual(to_list(reverse(build(values))), values[::-1])

    def test_no_cycle_after_reverse(self):
        head = reverse(build([1, 2, 3]))
        self.assertEqual(to_list(head), [3, 2, 1])  # to_list 有环检测，能过说明无环


class TestReverseRecursive(unittest.TestCase):
    def test_degenerate(self):
        self.assertIsNone(reverse_recursive(None))
        self.assertEqual(to_list(reverse_recursive(build([1]))), [1])

    def test_normal(self):
        self.assertEqual(to_list(reverse_recursive(build([1, 2, 3, 4, 5]))), [5, 4, 3, 2, 1])

    def test_agrees_with_iterative(self):
        values = [9, 8, 7, 6, 5, 4, 3]
        self.assertEqual(
            to_list(reverse_recursive(build(values))),
            to_list(reverse(build(values))),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

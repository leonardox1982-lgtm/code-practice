# -*- coding: utf-8 -*-
"""01 · 栈与队列 —— 单元测试。

跑测试：在本目录下执行 `python -m unittest -v`
"""

import unittest

from solution import Queue, Stack, is_balanced


class TestStack(unittest.TestCase):
    def test_lifo_order(self):
        s = Stack()
        s.push(1).push(2).push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_push_returns_self(self):
        s = Stack()
        self.assertIs(s.push("x"), s)

    def test_peek_does_not_remove(self):
        s = Stack()
        s.push("top")
        self.assertEqual(s.peek(), "top")
        self.assertEqual(len(s), 1)

    def test_len_and_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        self.assertEqual(len(s), 0)
        s.push(0)
        self.assertFalse(s.is_empty())
        self.assertEqual(len(s), 1)

    def test_to_list_is_bottom_to_top(self):
        s = Stack()
        s.push("a").push("b").push("c")
        self.assertEqual(s.to_list(), ["a", "b", "c"])

    def test_empty_pop_raises(self):
        with self.assertRaises(IndexError):
            Stack().pop()

    def test_empty_peek_raises(self):
        with self.assertRaises(IndexError):
            Stack().peek()

    def test_repr(self):
        s = Stack()
        s.push(1)
        self.assertIn("1", repr(s))


class TestQueue(unittest.TestCase):
    def test_fifo_order(self):
        q = Queue()
        q.enqueue(1).enqueue(2).enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)

    def test_enqueue_returns_self(self):
        q = Queue()
        self.assertIs(q.enqueue("x"), q)

    def test_peek_does_not_remove(self):
        q = Queue()
        q.enqueue("first")
        self.assertEqual(q.peek(), "first")
        self.assertEqual(len(q), 1)

    def test_to_list_is_front_to_rear(self):
        q = Queue()
        q.enqueue("a").enqueue("b").enqueue("c")
        self.assertEqual(q.to_list(), ["a", "b", "c"])

    def test_len_and_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(1)
        self.assertFalse(q.is_empty())
        self.assertEqual(len(q), 1)

    def test_empty_dequeue_raises(self):
        with self.assertRaises(IndexError):
            Queue().dequeue()

    def test_empty_peek_raises(self):
        with self.assertRaises(IndexError):
            Queue().peek()

    def test_many_items_stay_in_order(self):
        q = Queue()
        for i in range(1000):
            q.enqueue(i)
        self.assertEqual([q.dequeue() for _ in range(1000)], list(range(1000)))


class TestIsBalanced(unittest.TestCase):
    def test_balanced(self):
        for text in ("", "()", "[]", "{}", "()[]{}", "a(b[c]{d})e", "{[()]}"):
            with self.subTest(text=text):
                self.assertTrue(is_balanced(text))

    def test_unbalanced(self):
        for text in ("(", ")", "(()", "([)]", "((", "))", "{]", "a(b"):
            with self.subTest(text=text):
                self.assertFalse(is_balanced(text))

    def test_digits_and_letters_ignored(self):
        self.assertTrue(is_balanced("123 abc"))
        self.assertTrue(is_balanced("if (a > 0) { print(a[0]) }"))


if __name__ == "__main__":
    unittest.main(verbosity=2)

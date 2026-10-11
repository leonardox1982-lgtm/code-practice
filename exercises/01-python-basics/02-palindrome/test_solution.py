# -*- coding: utf-8 -*-
"""02 · 回文判断 —— 单元测试。

跑测试：在本目录下执行 `python -m unittest -v`
"""

import unittest

from solution import is_palindrome, normalize


class TestNormalize(unittest.TestCase):
    def test_keeps_only_alnum(self):
        self.assertEqual(normalize("A man, a plan, a canal: Panama"), "amanaplanacanalpanama")

    def test_lowercases(self):
        self.assertEqual(normalize("AbC123"), "abc123")

    def test_drops_punctuation_and_spaces(self):
        self.assertEqual(normalize("  a_b-c.d!e? "), "abcde")

    def test_keeps_cjk(self):
        self.assertEqual(normalize("上海 自来水"), "上海自来水")

    def test_empty(self):
        self.assertEqual(normalize(""), "")
        self.assertEqual(normalize("   ,.! "), "")


class TestIsPalindrome(unittest.TestCase):
    def test_classic_true(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_classic_false(self):
        self.assertFalse(is_palindrome("race a car"))

    def test_simple_true(self):
        for s in ("a", "aa", "aba", "abba", "Level", "Was it a car or a cat I saw?"):
            with self.subTest(s=s):
                self.assertTrue(is_palindrome(s))

    def test_simple_false(self):
        for s in ("ab", "abc", "abca", "0P", "hello"):
            with self.subTest(s=s):
                self.assertFalse(is_palindrome(s))

    def test_cjk(self):
        self.assertTrue(is_palindrome("上海自来水来自海上"))
        self.assertTrue(is_palindrome("人人为我我为人人"))
        self.assertFalse(is_palindrome("上海自来水"))

    def test_empty_is_palindrome(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("  ;;  "))
        self.assertTrue(is_palindrome("12321"))


if __name__ == "__main__":
    unittest.main(verbosity=2)

# -*- coding: utf-8 -*-
"""03 · 词频统计 —— 单元测试。

跑测试：在本目录下执行 `python -m unittest -v`
"""

import unittest

from solution import top_n, word_count

SAMPLE = """
It was the best of times, it was the worst of times,
it was the age of wisdom, it was the age of foolishness.
"""


class TestWordCount(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(
            word_count("The cat and the hat."),
            {"the": 2, "cat": 1, "and": 1, "hat": 1},
        )

    def test_case_insensitive(self):
        self.assertEqual(word_count("The THE the"), {"the": 3})

    def test_punctuation_stripped(self):
        result = word_count("hat. hat, hat! (hat)")
        self.assertEqual(result, {"hat": 4})

    def test_apostrophe_kept(self):
        self.assertEqual(word_count("don't don't cant"), {"don't": 2, "cant": 1})

    def test_digits_ignored(self):
        self.assertEqual(word_count("abc 123 xyz9"), {"abc": 1, "xyz": 1})

    def test_empty(self):
        self.assertEqual(word_count(""), {})
        self.assertEqual(word_count("123 !!! ..."), {})

    def test_sample_text(self):
        counts = word_count(SAMPLE)
        self.assertEqual(counts["it"], 4)
        self.assertEqual(counts["was"], 4)
        self.assertEqual(counts["the"], 4)
        self.assertEqual(counts["age"], 2)
        self.assertEqual(counts["of"], 4)


class TestTopN(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(top_n("b a b c a b", 2), [("b", 3), ("a", 2)])

    def test_tie_break_is_alphabetical(self):
        # a / b / c 各出现 1 次 → 按字母升序
        self.assertEqual(top_n("c b a", 3), [("a", 1), ("b", 1), ("c", 1)])

    def test_n_larger_than_vocab(self):
        self.assertEqual(top_n("a b", 10), [("a", 1), ("b", 1)])

    def test_degenerate_n(self):
        self.assertEqual(top_n("a b c", 0), [])
        self.assertEqual(top_n("a b c", -1), [])

    def test_sample_text(self):
        result = top_n(SAMPLE, 3)
        self.assertEqual([w for w, _ in result], ["it", "of", "the"])
        self.assertEqual([c for _, c in result], [4, 4, 4])


if __name__ == "__main__":
    unittest.main(verbosity=2)

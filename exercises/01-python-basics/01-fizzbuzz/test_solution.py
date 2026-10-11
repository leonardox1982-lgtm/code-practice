# -*- coding: utf-8 -*-
"""01 · FizzBuzz —— 单元测试。

跑测试：在本目录下执行 `python -m unittest -v`
"""

import unittest

from solution import fizzbuzz, fizzbuzz_list


class TestFizzBuzz(unittest.TestCase):
    def test_multiples_of_15(self):
        for n in (15, 30, 45, 150, 900):
            with self.subTest(n=n):
                self.assertEqual(fizzbuzz(n), "FizzBuzz")

    def test_multiples_of_3(self):
        for n in (3, 6, 9, 12, 33):
            with self.subTest(n=n):
                self.assertEqual(fizzbuzz(n), "Fizz")

    def test_multiples_of_5(self):
        for n in (5, 10, 20, 100):
            with self.subTest(n=n):
                self.assertEqual(fizzbuzz(n), "Buzz")

    def test_plain_numbers(self):
        for n in (1, 2, 4, 7, 11, 98):
            with self.subTest(n=n):
                self.assertEqual(fizzbuzz(n), str(n))

    def test_list_length_and_edges(self):
        result = fizzbuzz_list(15)
        self.assertEqual(len(result), 15)
        self.assertEqual(result[0], "1")
        self.assertEqual(result[2], "Fizz")
        self.assertEqual(result[4], "Buzz")
        self.assertEqual(result[-1], "FizzBuzz")

    def test_list_degenerate_inputs(self):
        self.assertEqual(fizzbuzz_list(1), ["1"])
        self.assertEqual(fizzbuzz_list(0), [])
        self.assertEqual(fizzbuzz_list(-5), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)

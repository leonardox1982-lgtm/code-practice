# -*- coding: utf-8 -*-
"""02 · 欧几里得算法与模逆元 —— 单元测试。

跑测试：在本目录下执行 `python -m unittest -v`
"""

import random
import unittest

from solution import extended_gcd, gcd, lcm, mod_inverse


class TestGcd(unittest.TestCase):
    def test_known_values(self):
        self.assertEqual(gcd(1071, 462), 21)
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(17, 5), 1)
        self.assertEqual(gcd(100, 100), 100)

    def test_zero(self):
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)

    def test_negative_returns_positive(self):
        self.assertEqual(gcd(-4, 6), 2)
        self.assertEqual(gcd(4, -6), 2)
        self.assertEqual(gcd(-4, -6), 2)

    def test_symmetry(self):
        rng = random.Random(20261011)
        for _ in range(200):
            a, b = rng.randrange(-10_000, 10_000), rng.randrange(-10_000, 10_000)
            with self.subTest(a=a, b=b):
                self.assertEqual(gcd(a, b), gcd(b, a))

    def test_divides_both(self):
        rng = random.Random(7)
        for _ in range(200):
            a, b = rng.randrange(1, 100_000), rng.randrange(1, 100_000)
            g = gcd(a, b)
            with self.subTest(a=a, b=b):
                self.assertEqual(a % g, 0)
                self.assertEqual(b % g, 0)


class TestLcm(unittest.TestCase):
    def test_known_values(self):
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(21, 6), 42)
        self.assertEqual(lcm(7, 13), 91)

    def test_zero(self):
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(5, 0), 0)
        self.assertEqual(lcm(0, 0), 0)

    def test_negative(self):
        self.assertEqual(lcm(-4, 6), 12)
        self.assertEqual(lcm(-4, -6), 12)

    def test_identity_with_gcd(self):
        rng = random.Random(11)
        for _ in range(200):
            a, b = rng.randrange(1, 5000), rng.randrange(1, 5000)
            with self.subTest(a=a, b=b):
                self.assertEqual(lcm(a, b) * gcd(a, b), a * b)


class TestExtendedGcd(unittest.TestCase):
    def test_bezout_identity_small(self):
        for a, b in ((240, 46), (30, 21), (7, 0), (0, 7), (0, 0), (1, 1)):
            with self.subTest(a=a, b=b):
                g, x, y = extended_gcd(a, b)
                self.assertEqual(a * x + b * y, g)
                self.assertEqual(g, gcd(a, b))

    def test_bezout_identity_with_negatives(self):
        for a, b in ((-240, 46), (240, -46), (-240, -46), (-1, 5)):
            with self.subTest(a=a, b=b):
                g, x, y = extended_gcd(a, b)
                self.assertEqual(a * x + b * y, g)
                self.assertEqual(g, gcd(a, b))

    def test_bezout_identity_random_big(self):
        rng = random.Random(2026)
        for _ in range(300):
            a = rng.randrange(-10**9, 10**9)
            b = rng.randrange(-10**9, 10**9)
            with self.subTest(a=a, b=b):
                g, x, y = extended_gcd(a, b)
                self.assertEqual(a * x + b * y, g)
                self.assertEqual(g, gcd(a, b))
                self.assertGreaterEqual(g, 0)


class TestModInverse(unittest.TestCase):
    def test_known_values(self):
        self.assertEqual(mod_inverse(3, 11), 4)
        self.assertEqual(mod_inverse(1, 7), 1)
        self.assertEqual(mod_inverse(10, 17), 12)   # 10*12 = 120 = 7*17+1

    def test_result_in_range(self):
        rng = random.Random(99)
        for _ in range(200):
            m = rng.randrange(2, 10_000)
            a = rng.randrange(1, m)
            if gcd(a, m) != 1:
                continue
            with self.subTest(a=a, m=m):
                x = mod_inverse(a, m)
                self.assertTrue(0 <= x < m)
                self.assertEqual((a * x) % m, 1)

    def test_no_inverse_raises(self):
        for a, m in ((2, 4), (2, 6), (3, 9), (6, 15)):
            with self.subTest(a=a, m=m):
                with self.assertRaises(ValueError):
                    mod_inverse(a, m)

    def test_bad_modulus_raises(self):
        for m in (1, 0, -5):
            with self.subTest(m=m):
                with self.assertRaises(ValueError):
                    mod_inverse(3, m)


if __name__ == "__main__":
    unittest.main(verbosity=2)

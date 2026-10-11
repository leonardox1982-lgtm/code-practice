# -*- coding: utf-8 -*-
"""01 · 素数筛与质因数分解 —— 单元测试。

跑测试：在本目录下执行 `python -m unittest -v`
"""

import math
import random
import unittest

from solution import count_primes, is_prime, prime_factors, sieve


class TestSieve(unittest.TestCase):
    def test_small(self):
        self.assertEqual(sieve(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_degenerate(self):
        self.assertEqual(sieve(0), [])
        self.assertEqual(sieve(1), [])
        self.assertEqual(sieve(-10), [])

    def test_boundary_inclusive(self):
        self.assertEqual(sieve(2), [2])
        self.assertEqual(sieve(3), [2, 3])
        self.assertEqual(sieve(4), [2, 3])
        self.assertEqual(sieve(5), [2, 3, 5])

    def test_count_below_one_million(self):
        self.assertEqual(count_primes(1_000_000), 78498)

    def test_first_and_last_prime_of_range(self):
        primes = sieve(100)
        self.assertEqual(primes[0], 2)
        self.assertEqual(primes[-1], 97)
        self.assertEqual(len(primes), 25)   # π(100) = 25


class TestIsPrime(unittest.TestCase):
    def test_known_primes(self):
        for n in (2, 3, 5, 7, 11, 13, 97, 7919):
            with self.subTest(n=n):
                self.assertTrue(is_prime(n))

    def test_known_composites(self):
        for n in (0, 1, 4, 6, 9, 15, 91, 7917):
            with self.subTest(n=n):
                self.assertFalse(is_prime(n))

    def test_negative(self):
        self.assertFalse(is_prime(-7))
        self.assertFalse(is_prime(-1))

    def test_square_of_prime(self):
        for p in (2, 3, 5, 7, 11, 101):
            with self.subTest(p=p):
                self.assertFalse(is_prime(p * p))

    def test_agrees_with_sieve(self):
        primes = set(sieve(2000))
        for n in range(-5, 2000):
            with self.subTest(n=n):
                self.assertEqual(is_prime(n), n in primes)


class TestPrimeFactors(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(prime_factors(12), [2, 2, 3])
        self.assertEqual(prime_factors(360), [2, 2, 2, 3, 3, 5])
        self.assertEqual(prime_factors(97), [97])
        self.assertEqual(prime_factors(1024), [2] * 10)

    def test_degenerate(self):
        self.assertEqual(prime_factors(0), [])
        self.assertEqual(prime_factors(1), [])

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            prime_factors(-12)

    def test_every_factor_is_prime(self):
        for n in (12, 360, 1024, 9999, 123456):
            with self.subTest(n=n):
                for f in prime_factors(n):
                    self.assertTrue(is_prime(f))

    def test_random_product_matches(self):
        rng = random.Random(20261011)
        for _ in range(300):
            n = rng.randrange(2, 200_000)
            factors = prime_factors(n)
            with self.subTest(n=n):
                self.assertEqual(math.prod(factors), n)
                self.assertEqual(factors, sorted(factors))


if __name__ == "__main__":
    unittest.main(verbosity=2)

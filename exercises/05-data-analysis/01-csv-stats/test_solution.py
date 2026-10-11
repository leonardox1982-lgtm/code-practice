# -*- coding: utf-8 -*-
"""01 · CSV 读取与描述统计 —— 单元测试。

跑测试：在本目录下执行 `python -m unittest -v`
"""

import csv
import statistics
import tempfile
import unittest
from pathlib import Path

from solution import (
    mean,
    median,
    read_rows,
    read_scores,
    stdev,
    summarize,
    to_floats,
)

DATA = Path(__file__).with_name("data") / "scores.csv"


class TestReadRows(unittest.TestCase):
    def test_reads_bundled_csv(self):
        rows = read_rows(DATA)
        self.assertEqual(len(rows), 8)
        self.assertEqual(rows[0]["name"], "张三")
        self.assertEqual(rows[0]["score"], "88")

    def test_handles_bom(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bom.csv"
            path.write_text("name,score\n甲,10\n", encoding="utf-8-sig")
            rows = read_rows(path)
            self.assertIn("name", rows[0])          # 列名不带 \ufeff
            self.assertEqual(rows[0]["score"], "10")

    def test_missing_file_raises(self):
        with self.assertRaises(FileNotFoundError):
            read_rows(Path("no/such/file.csv"))


class TestToFloats(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(to_floats(["1", "2.5"]), [1.0, 2.5])

    def test_skips_missing_markers(self):
        self.assertEqual(to_floats(["1", "", None, "-", "N/A", "2"]), [1.0, 2.0])

    def test_strips_whitespace(self):
        self.assertEqual(to_floats([" 3 ", "\t4\n"]), [3.0, 4.0])

    def test_bad_value_raises_with_context(self):
        with self.assertRaises(ValueError) as ctx:
            to_floats(["1", "abc"])
        self.assertIn("abc", str(ctx.exception))

    def test_accepts_numbers(self):
        self.assertEqual(to_floats([1, 2.5]), [1.0, 2.5])

    def test_all_missing_gives_empty(self):
        self.assertEqual(to_floats(["-", "", None]), [])


class TestStatistics(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([1, 2, 3]), 2)
        self.assertEqual(mean([1, 2, 3, 4]), 2.5)
        self.assertAlmostEqual(mean([0.1] * 10), 0.1, places=12)

    def test_median_odd_and_even(self):
        self.assertEqual(median([3, 1, 2]), 2)
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        self.assertEqual(median([4, 1]), 2.5)

    def test_median_does_not_mutate(self):
        data = [3, 1, 2]
        median(data)
        self.assertEqual(data, [3, 1, 2])

    def test_stdev_matches_statistics_module(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        self.assertAlmostEqual(stdev(data), statistics.stdev(data), places=12)
        self.assertAlmostEqual(stdev(data, sample=False), statistics.pstdev(data), places=12)

    def test_stdev_edge_cases(self):
        self.assertEqual(stdev([]), 0.0)
        self.assertEqual(stdev([5]), 0.0)
        self.assertEqual(stdev([5, 5, 5]), 0.0)

    def test_empty_raises(self):
        for fn in (mean, median):
            with self.subTest(fn=fn.__name__):
                with self.assertRaises(ValueError):
                    fn([])

    def test_constant_series(self):
        self.assertEqual(mean([7] * 5), 7)
        self.assertEqual(median([7] * 5), 7)


class TestSummarize(unittest.TestCase):
    def test_bundled_scores(self):
        stats = summarize(read_scores(DATA))
        self.assertEqual(stats["count"], 8)
        self.assertAlmostEqual(stats["mean"], 82.875, places=10)
        self.assertAlmostEqual(stats["median"], 85.5, places=10)
        self.assertAlmostEqual(stats["min"], 61.5, places=10)
        self.assertAlmostEqual(stats["max"], 95.0, places=10)
        # 与标准库交叉校验（样本标准差，ddof=1）
        self.assertAlmostEqual(stats["stdev"], statistics.stdev(read_scores(DATA)), places=10)

    def test_keys(self):
        stats = summarize([1, 2, 3])
        self.assertEqual(
            set(stats),
            {"count", "mean", "median", "min", "max", "stdev"},
        )

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            summarize([])


class TestReadScores(unittest.TestCase):
    def test_bundled(self):
        self.assertEqual(
            read_scores(DATA),
            [88.0, 92.5, 79.0, 95.0, 61.5, 83.0, 74.0, 90.0],
        )

    def test_custom_column(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "d.csv"
            with open(path, "w", newline="", encoding="utf-8") as fh:
                writer = csv.writer(fh)
                writer.writerow(["a", "b"])
                writer.writerow(["1", "10"])
                writer.writerow(["-", "20"])
            self.assertEqual(read_scores(path, "b"), [10.0, 20.0])
            self.assertEqual(read_scores(path, "a"), [1.0])


if __name__ == "__main__":
    unittest.main(verbosity=2)

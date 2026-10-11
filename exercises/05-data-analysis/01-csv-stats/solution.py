# -*- coding: utf-8 -*-
"""01 · CSV 读取与描述统计

【你的作答区】把下面的函数体补全，然后在本目录跑：

    python -m unittest -v

- 题面：同目录的 README.md
- 对答案（不改动文件）：python tools/reference.py show 01-csv-stats
- 从零重来：python tools/reference.py blank 01-csv-stats
- 还原参考实现：python tools/reference.py restore 01-csv-stats
"""
import csv
import math
from collections.abc import Iterable
from pathlib import Path
MISSING = {'', '-', 'n/a', 'N/A', 'null', 'None', 'NA'}


def read_rows(path: str | Path) -> list[dict[str, str]]:
    """读取 CSV，返回「列名 → 字符串」的行列表。utf-8-sig 用来吃掉 BOM。"""
    raise NotImplementedError('TODO: 实现 read_rows')


def to_floats(values: Iterable) -> list[float]:
    """把一列值转成浮点数，缺失值跳过。"""
    raise NotImplementedError('TODO: 实现 to_floats')


def _require_non_empty(xs: list[float]) -> None:
    raise NotImplementedError('TODO: 实现 _require_non_empty')


def mean(xs: Iterable) -> float:
    """算术平均。"""
    raise NotImplementedError('TODO: 实现 mean')


def median(xs: Iterable) -> float:
    """中位数。"""
    raise NotImplementedError('TODO: 实现 median')


def stdev(xs: Iterable, sample: bool=True) -> float:
    """标准差。sample=True 用 n-1，False 用 n；少于 2 个元素返回 0.0。"""
    raise NotImplementedError('TODO: 实现 stdev')


def summarize(values: Iterable) -> dict:
    """一次给出 count / mean / median / min / max / stdev。"""
    raise NotImplementedError('TODO: 实现 summarize')


def read_scores(path: str | Path, column: str='score') -> list[float]:
    """读 CSV 的某一列并转成浮点数。"""
    raise NotImplementedError('TODO: 实现 read_scores')


if __name__ == '__main__':
    csv_path = Path(__file__).with_name('data') / 'scores.csv'
    scores = read_scores(csv_path)
    print('分数:', scores)
    stats = summarize(scores)
    for key, value in stats.items():
        print(f'  {key:>7}: {value}')

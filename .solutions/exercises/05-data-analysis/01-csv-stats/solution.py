# -*- coding: utf-8 -*-
"""01 · CSV 读取与描述统计

自己先写一版，然后把这里替换掉。
卡住了就 `git checkout -- exercises/05-data-analysis/01-csv-stats/solution.py` 回到参考实现。
"""

import csv
import math
from collections.abc import Iterable
from pathlib import Path

MISSING = {"", "-", "n/a", "N/A", "null", "None", "NA"}


def read_rows(path: str | Path) -> list[dict[str, str]]:
    """读取 CSV，返回「列名 → 字符串」的行列表。utf-8-sig 用来吃掉 BOM。"""
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def to_floats(values: Iterable) -> list[float]:
    """把一列值转成浮点数，缺失值跳过。"""
    out: list[float] = []
    for raw in values:
        if raw is None:
            continue
        text = str(raw).strip()
        if text in MISSING:
            continue
        try:
            out.append(float(text))
        except ValueError as exc:
            raise ValueError(f"无法解析为数字: {raw!r}") from exc
    return out


def _require_non_empty(xs: list[float]) -> None:
    if not xs:
        raise ValueError("数据为空，无法计算")


def mean(xs: Iterable) -> float:
    """算术平均。"""
    data = to_floats(xs)
    _require_non_empty(data)
    return sum(data) / len(data)


def median(xs: Iterable) -> float:
    """中位数。"""
    data = sorted(to_floats(xs))
    _require_non_empty(data)
    n = len(data)
    mid = n // 2
    if n % 2:
        return float(data[mid])
    return (data[mid - 1] + data[mid]) / 2


def stdev(xs: Iterable, sample: bool = True) -> float:
    """标准差。sample=True 用 n-1，False 用 n；少于 2 个元素返回 0.0。"""
    data = to_floats(xs)
    n = len(data)
    if n < 2:
        return 0.0
    avg = sum(data) / n
    variance = sum((x - avg) ** 2 for x in data) / (n - 1 if sample else n)
    return math.sqrt(variance)


def summarize(values: Iterable) -> dict:
    """一次给出 count / mean / median / min / max / stdev。"""
    data = to_floats(values)
    _require_non_empty(data)
    return {
        "count": len(data),
        "mean": mean(data),
        "median": median(data),
        "min": float(min(data)),
        "max": float(max(data)),
        "stdev": stdev(data),
    }


def read_scores(path: str | Path, column: str = "score") -> list[float]:
    """读 CSV 的某一列并转成浮点数。"""
    rows = read_rows(path)
    return to_floats(row.get(column) for row in rows)


if __name__ == "__main__":
    csv_path = Path(__file__).with_name("data") / "scores.csv"
    scores = read_scores(csv_path)
    print("分数:", scores)
    stats = summarize(scores)
    for key, value in stats.items():
        print(f"  {key:>7}: {value}")

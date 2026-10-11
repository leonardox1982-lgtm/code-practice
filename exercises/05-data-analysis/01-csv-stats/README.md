# 01 · CSV 读取与描述统计

**赛道**：05-data-analysis
**考点**：`csv` 模块、字典序列、均值/中位数/标准差、异常数据

> 这是后面做真实数据（订单、销售、问卷）时的最小可用积木。比起直接上 pandas，
> 先用标准库手写一遍，你对「一列数据是怎么变成统计量的」会清楚得多。

## 题目

1. `read_rows(path: str | Path) -> list[dict[str, str]]`
   - 用 `csv.DictReader` 读取，返回「列名 → 单元格字符串」的行列表；
   - 文件用 `utf-8-sig` 打开（**这是关键**：Windows 导出的 CSV 常带 BOM，不处理第一列列名会变成 `\ufeffname`）。

2. `to_floats(values: Iterable) -> list[float]`
   - 把一列值转成浮点数；空串、`None`、`"-"`、`"N/A"` 一律**跳过**（不报错）；
   - 无法解析的其他内容抛 `ValueError`，消息里带上出错的原值。

3. 统计量（空列表一律抛 `ValueError`，除了 `stdev` 的 1 个元素情况见下）：
   - `mean(xs) -> float`：算术平均
   - `median(xs) -> float`：中位数（偶数个取中间两个的平均）
   - `stdev(xs, sample: bool = True) -> float`：标准差。`sample=True` 用 n-1（样本），`False` 用 n（总体）；2 个以下元素时返回 `0.0`

4. `summarize(xs) -> dict`：返回

   ```python
   {"count": int, "mean": float, "median": float,
    "min": float, "max": float, "stdev": float}
   ```

5. `read_scores(path, column: str = "score") -> list[float]`
   - 读 CSV 并取出某一列转成浮点数，把前面几步串起来。

## 示例

```python
>>> read_scores("data/scores.csv")
[88.0, 92.5, 79.0, 95.0, 61.5, 83.0, 74.0, 90.0]
>>> round(mean([1, 2, 3, 4]), 2)
2.5
>>> median([1, 2, 3, 4])
2.5
>>> summarize([1, 2, 3, 4])["count"]
4
```

## 提示

- 读文件的正确姿势：

  ```python
  with open(path, newline="", encoding="utf-8-sig") as fh:
      return list(csv.DictReader(fh))
  ```

  `newline=""` 是 `csv` 模块文档明确要求的，不加在 Windows 上会出现多余空行。

- 标准差的定义差别很大，写之前先想清楚：

  ```
  样本标准差 s = sqrt( Σ(xᵢ - x̄)² / (n - 1) )
  总体标准差 σ = sqrt( Σ(xᵢ - x̄)² / n )
  ```

  数据是「全部总体」用 n，是「抽样得来」用 n-1。日常分析里默认 n-1。

- **别用 `sum(xs) / len(xs)` 的方式算方差**，浮点误差会累积。可以两遍扫描（先算均值再算偏差平方和），也可以自己检查一下和 `statistics.stdev` 是否一致。
- 中位数记得先排序：`sorted(xs)`。

## 验收标准

- [ ] `python -m unittest -v` 全部通过
- [ ] `data/scores.csv` 的均值是 82.875、中位数是 85.5
- [ ] 结果与标准库 `statistics` 模块一致（测试里会交叉校验）
- [ ] 空列表抛 `ValueError`；脏数据（`""` / `"-"` / `"N/A"`）被跳过

## 参考

`statistics` 模块文档；《利用 Python 进行数据分析》第 5 章（pandas 入门，本题是它的手写版）

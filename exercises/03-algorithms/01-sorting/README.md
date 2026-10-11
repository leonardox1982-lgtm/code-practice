# 01 · 排序（分治）

**赛道**：03-algorithms
**考点**：分治思想、递归、稳定性、时间复杂度

## 题目

实现两个排序函数，都返回**新列表**，不修改入参：

1. `quick_sort(nums: list) -> list`
   - 用三路划分（小于 / 等于 / 大于主元）的写法，避免元素大量重复时退化。
   - 主元随便选一个，建议取中间元素。

2. `merge_sort(nums: list) -> list`
   - 归并排序，并把它拆出一个可单独测试的辅助函数：

     `merge(left: list, right: list) -> list`
     - 合并两个**已排序**列表，返回新的有序列表；
     - 相等元素**先取左边的**（这就是归并排序「稳定」的原因）。

## 示例

```python
>>> quick_sort([3, 1, 2])
[1, 2, 3]
>>> merge_sort([3, 1, 2])
[1, 2, 3]
>>> merge([1, 3, 5], [2, 4])
[1, 2, 3, 4, 5]
```

## 提示

三路快排的骨架（这样写对重复元素特别友好，也不会因为主元选得差而递归不下去）：

```python
def quick_sort(nums):
    if len(nums) <= 1:
        return list(nums)
    pivot = nums[len(nums) // 2]
    less    = [x for x in nums if x < pivot]
    equal   = [x for x in nums if x == pivot]
    greater = [x for x in nums if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)
```

归并的骨架：

```python
def merge(left, right):
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:      # <= 才稳定
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out
```

## 复杂度对照

| 算法 | 平均 | 最坏 | 额外空间 | 稳定 |
| --- | --- | --- | --- | --- |
| 三路快排 | O(n log n) | O(n²) | O(n)（上面这种写法） | 否 |
| 归并排序 | O(n log n) | O(n log n) | O(n) | **是** |

> 顺带想一个面试常问的问题：**为什么 `list.sort()` 用 Timsort 而不用快排？**（提示：真实数据常常「接近有序」，Timsort 能利用这一点。）

## 验收标准

- [ ] `python -m unittest -v` 全部通过
- [ ] 空列表、单元素、全相同元素都不崩
- [ ] 随机对拍：结果必须等于内置 `sorted()`
- [ ] `merge` 可被单独调用并测试

## 参考

MIT 6.042J Ch.15 递归式分析（快排的期望复杂度）；《算法导论》第 2、7 章

# 03 · 最大子数组和

**赛道**：03-algorithms
**考点**：动态规划 / Kadane 算法、原地状态转移

## 题目

实现两个函数：

1. `max_subarray(nums: list[int]) -> int`
   - 返回**非空**连续子数组的最大和。
   - 空列表抛 `ValueError`。

2. `max_subarray_range(nums: list[int]) -> tuple[int, int, int]`
   - 返回 `(最大和, 起始下标, 结束下标)`，**结束下标不含**（即切片 `nums[start:end]`）。
   - 有并列最优时，返回**最靠前**的那一段。

要求 O(n) 时间。

## 示例

```python
>>> max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
6
>>> max_subarray_range([-2, 1, -3, 4, -1, 2, 1, -5, 4])
(6, 3, 7)
>>> max_subarray([-3, -1, -2])       # 全负也要选一个
-1
>>> max_subarray_range([-3, -1, -2])
(-1, 1, 2)
```

## 提示

Kadane 的核心只有一行：

```python
cur = max(x, cur + x)   # 要么「接着前面的段」，要么「从 x 重新开一段」
```

完整骨架：

```python
best = cur = nums[0]
for x in nums[1:]:
    cur = max(x, cur + x)
    best = max(best, cur)
```

要同时记录区间时，关键是在**重新开一段的那一刻**把 `cur_start` 更新为当前下标：

```python
if cur + x < x:          # 说明不如从 x 重新开始
    cur = x
    cur_start = i
else:
    cur += x
if cur > best:           # 严格大于 → 并列时保留更靠前的那段
    best = cur
    best_start, best_end = cur_start, i + 1
```

**别被「全负数」坑到**：如果用 `best = 0` 初始化，`[-3, -1, -2]` 会错误地返回 `0`，但题目要求子数组非空，答案应该是 `-1`。

## 验收标准

- [ ] `python -m unittest -v` 全部通过
- [ ] 空列表抛 `ValueError`
- [ ] 全负数数组返回最大的那个负数
- [ ] `max_subarray_range` 返回的区间切片求和必须等于 `max_subarray`
- [ ] 随机对拍：与 O(n²) 暴力解法结果一致

## 参考

LeetCode 53. Maximum Subarray；《编程珠玑》第 8 章

# 03 · 二分查找与边界

**赛道**：02-data-structures
**考点**：二分不变量、`lo`/`hi` 的取法、重复元素下的左右边界

## 题目

给定**升序**（非降序）整数列表，实现三个函数：

1. `binary_search(nums: list[int], target: int) -> int`
   - 找到返回任意一个匹配下标；找不到返回 `-1`。

2. `lower_bound(nums: list[int], target: int) -> int`
   - 返回**第一个 ≥ target** 的下标；若全部小于 `target`，返回 `len(nums)`。
   - 等价于：`target` 应该插入的位置（保持有序）。

3. `upper_bound(nums: list[int], target: int) -> int`
   - 返回**第一个 > target** 的下标；若全部 ≤ `target`，返回 `len(nums)`。

## 示例

```python
>>> nums = [1, 2, 2, 2, 3, 5]
>>> lower_bound(nums, 2)
1
>>> upper_bound(nums, 2)
4
>>> nums[1:4]          # 这就是「2 的出现区间」
[2, 2, 2]
>>> binary_search(nums, 3)
4
>>> binary_search(nums, 4)
-1
```

## 提示

- 三个函数可以共用一套骨架，**只改「命中时怎么动」**：

  ```python
  lo, hi = 0, len(nums)          # 注意 hi 是开区间，取 len 而不是 len-1
  while lo < hi:
      mid = (lo + hi) // 2
      if nums[mid] < target:
          lo = mid + 1
      else:
          hi = mid               # lower_bound：命中也不停，继续往左压
  return lo
  ```

- `upper_bound` 只需把条件改成 `nums[mid] <= target`。
- `binary_search` 可以用 `lower_bound` 直接实现：

  ```python
  i = lower_bound(nums, target)
  return i if i < len(nums) and nums[i] == target else -1
  ```

- **别用 `mid = (lo + hi) / 2`**（会变浮点），也别在 `while lo <= hi` 的闭区间写法里漏掉 `mid ± 1`，那是死循环和差一错误的重灾区。
- 出现次数 = `upper_bound(t) - lower_bound(t)`。

## 验收标准

- [ ] `python -m unittest -v` 全部通过
- [ ] 空列表返回 `0` / `-1`（不要崩）
- [ ] 重复元素下 `lower_bound` / `upper_bound` 精确落在区间边界
- [ ] 建议加上 `test_performance` 里那种「和暴力解法对拍」的随机测试

## 参考

CPython `bisect` 模块源码（`bisect_left` / `bisect_right` 就是本题的 `lower_bound` / `upper_bound`）

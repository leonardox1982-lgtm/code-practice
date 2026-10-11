# -*- coding: utf-8 -*-
"""03 · 二分查找与边界

自己先写一版，然后把这里替换掉。
卡住了就 `git checkout -- exercises/02-data-structures/03-binary-search/solution.py` 回到参考实现。
"""


def lower_bound(nums: list[int], target: int) -> int:
    """返回第一个 >= target 的下标；全部小于时返回 len(nums)。"""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(nums: list[int], target: int) -> int:
    """返回第一个 > target 的下标；全部 <= target 时返回 len(nums)。"""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def binary_search(nums: list[int], target: int) -> int:
    """找到返回下标，找不到返回 -1。"""
    i = lower_bound(nums, target)
    if i < len(nums) and nums[i] == target:
        return i
    return -1


def count_occurrences(nums: list[int], target: int) -> int:
    """target 在有序列表中出现的次数（O(log n)）。"""
    return upper_bound(nums, target) - lower_bound(nums, target)


if __name__ == "__main__":
    nums = [1, 2, 2, 2, 3, 5]
    print("nums =", nums)
    for t in (1, 2, 3, 4, 5, 6):
        print(f"target={t}: lower={lower_bound(nums, t)} "
              f"upper={upper_bound(nums, t)} "
              f"search={binary_search(nums, t)} "
              f"count={count_occurrences(nums, t)}")

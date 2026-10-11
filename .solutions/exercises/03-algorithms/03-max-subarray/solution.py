# -*- coding: utf-8 -*-
"""03 · 最大子数组和

自己先写一版，然后把这里替换掉。
卡住了就 `git checkout -- exercises/03-algorithms/03-max-subarray/solution.py` 回到参考实现。
"""


def max_subarray(nums: list[int]) -> int:
    """非空连续子数组的最大和，O(n)。"""
    if not nums:
        raise ValueError("nums must not be empty")
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


def max_subarray_range(nums: list[int]) -> tuple[int, int, int]:
    """返回 (最大和, 起始下标, 结束下标)，结束下标不含；并列时取最靠前的一段。"""
    if not nums:
        raise ValueError("nums must not be empty")

    best = cur = nums[0]
    best_start, best_end = 0, 1
    cur_start = 0

    for i in range(1, len(nums)):
        x = nums[i]
        if cur + x < x:
            cur = x
            cur_start = i
        else:
            cur += x
        if cur > best:
            best = cur
            best_start, best_end = cur_start, i + 1

    return best, best_start, best_end


def max_subarray_bruteforce(nums: list[int]) -> int:
    """O(n²) 暴力解法，只用来自检和对拍。"""
    if not nums:
        raise ValueError("nums must not be empty")
    best = nums[0]
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            best = max(best, total)
    return best


if __name__ == "__main__":
    data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("数组          :", data)
    print("最大子数组和  :", max_subarray(data))
    total, start, end = max_subarray_range(data)
    print(f"最优区间      : nums[{start}:{end}] = {data[start:end]} -> {total}")
    print("全负数组      :", max_subarray([-3, -1, -2]), max_subarray_range([-3, -1, -2]))

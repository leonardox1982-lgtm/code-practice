# -*- coding: utf-8 -*-
"""01 · 排序（分治）

自己先写一版，然后把这里替换掉。
卡住了就 `git checkout -- exercises/03-algorithms/01-sorting/solution.py` 回到参考实现。
"""


def quick_sort(nums: list) -> list:
    """三路划分快排。返回新列表，O(n log n) 平均、对重复元素友好。"""
    if len(nums) <= 1:
        return list(nums)
    pivot = nums[len(nums) // 2]
    less = [x for x in nums if x < pivot]
    equal = [x for x in nums if x == pivot]
    greater = [x for x in nums if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)


def merge(left: list, right: list) -> list:
    """合并两个已排序列表；相等时先取左边，保证稳定。"""
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out


def merge_sort(nums: list) -> list:
    """归并排序。稳定，最坏也是 O(n log n)。"""
    if len(nums) <= 1:
        return list(nums)
    mid = len(nums) // 2
    return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))


if __name__ == "__main__":
    import random

    rng = random.Random(42)
    data = [rng.randrange(100) for _ in range(20)]
    print("原始:", data)
    print("快排:", quick_sort(data))
    print("归并:", merge_sort(data))
    print("内置:", sorted(data))

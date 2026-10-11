# -*- coding: utf-8 -*-
"""03 · 二分查找与边界

【你的作答区】把下面的函数体补全，然后在本目录跑：

    python -m unittest -v

- 题面：同目录的 README.md
- 对答案（不改动文件）：python tools/reference.py show 03-binary-search
- 从零重来：python tools/reference.py blank 03-binary-search
- 还原参考实现：python tools/reference.py restore 03-binary-search
"""


def lower_bound(nums: list[int], target: int) -> int:
    """返回第一个 >= target 的下标；全部小于时返回 len(nums)。"""
    raise NotImplementedError('TODO: 实现 lower_bound')


def upper_bound(nums: list[int], target: int) -> int:
    """返回第一个 > target 的下标；全部 <= target 时返回 len(nums)。"""
    raise NotImplementedError('TODO: 实现 upper_bound')


def binary_search(nums: list[int], target: int) -> int:
    """找到返回下标，找不到返回 -1。"""
    raise NotImplementedError('TODO: 实现 binary_search')


def count_occurrences(nums: list[int], target: int) -> int:
    """target 在有序列表中出现的次数（O(log n)）。"""
    raise NotImplementedError('TODO: 实现 count_occurrences')


if __name__ == '__main__':
    nums = [1, 2, 2, 2, 3, 5]
    print('nums =', nums)
    for t in (1, 2, 3, 4, 5, 6):
        print(f'target={t}: lower={lower_bound(nums, t)} upper={upper_bound(nums, t)} search={binary_search(nums, t)} count={count_occurrences(nums, t)}')

# -*- coding: utf-8 -*-
"""01 · 排序（分治）

【你的作答区】把下面的函数体补全，然后在本目录跑：

    python -m unittest -v

- 题面：同目录的 README.md
- 对答案（不改动文件）：python tools/reference.py show 01-sorting
- 从零重来：python tools/reference.py blank 01-sorting
- 还原参考实现：python tools/reference.py restore 01-sorting
"""


def quick_sort(nums: list) -> list:
    """三路划分快排。返回新列表，O(n log n) 平均、对重复元素友好。"""
    raise NotImplementedError('TODO: 实现 quick_sort')


def merge(left: list, right: list) -> list:
    """合并两个已排序列表；相等时先取左边，保证稳定。"""
    raise NotImplementedError('TODO: 实现 merge')


def merge_sort(nums: list) -> list:
    """归并排序。稳定，最坏也是 O(n log n)。"""
    raise NotImplementedError('TODO: 实现 merge_sort')


if __name__ == '__main__':
    import random
    rng = random.Random(42)
    data = [rng.randrange(100) for _ in range(20)]
    print('原始:', data)
    print('快排:', quick_sort(data))
    print('归并:', merge_sort(data))
    print('内置:', sorted(data))

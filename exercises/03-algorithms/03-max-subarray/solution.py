# -*- coding: utf-8 -*-
"""03 · 最大子数组和

【你的作答区】把下面的函数体补全，然后在本目录跑：

    python -m unittest -v

- 题面：同目录的 README.md
- 对答案（不改动文件）：python tools/reference.py show 03-max-subarray
- 从零重来：python tools/reference.py blank 03-max-subarray
- 还原参考实现：python tools/reference.py restore 03-max-subarray
"""


def max_subarray(nums: list[int]) -> int:
    """非空连续子数组的最大和，O(n)。"""
    raise NotImplementedError('TODO: 实现 max_subarray')


def max_subarray_range(nums: list[int]) -> tuple[int, int, int]:
    """返回 (最大和, 起始下标, 结束下标)，结束下标不含；并列时取最靠前的一段。"""
    raise NotImplementedError('TODO: 实现 max_subarray_range')


def max_subarray_bruteforce(nums: list[int]) -> int:
    """O(n²) 暴力解法，只用来自检和对拍。"""
    raise NotImplementedError('TODO: 实现 max_subarray_bruteforce')


if __name__ == '__main__':
    data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print('数组          :', data)
    print('最大子数组和  :', max_subarray(data))
    total, start, end = max_subarray_range(data)
    print(f'最优区间      : nums[{start}:{end}] = {data[start:end]} -> {total}')
    print('全负数组      :', max_subarray([-3, -1, -2]), max_subarray_range([-3, -1, -2]))

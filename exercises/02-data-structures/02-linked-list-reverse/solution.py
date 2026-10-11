# -*- coding: utf-8 -*-
"""02 · 单链表反转

【你的作答区】把下面的函数体补全，然后在本目录跑：

    python -m unittest -v

- 题面：同目录的 README.md
- 对答案（不改动文件）：python tools/reference.py show 02-linked-list-reverse
- 从零重来：python tools/reference.py blank 02-linked-list-reverse
- 还原参考实现：python tools/reference.py restore 02-linked-list-reverse
"""


class Node:
    """单向链表节点。"""
    __slots__ = ('value', 'next')

    def __init__(self, value, next: 'Node | None'=None) -> None:
        raise NotImplementedError('TODO: 实现 __init__')

    def __repr__(self) -> str:
        raise NotImplementedError('TODO: 实现 __repr__')


def build(values: list) -> 'Node | None':
    """把列表串成链表，返回头节点。"""
    raise NotImplementedError('TODO: 实现 build')


def to_list(head: 'Node | None') -> list:
    """把链表转回列表；检测到环则报错。"""
    raise NotImplementedError('TODO: 实现 to_list')


def reverse(head: 'Node | None') -> 'Node | None':
    """原地反转链表，返回新头节点。O(n) 时间、O(1) 额外空间。"""
    raise NotImplementedError('TODO: 实现 reverse')


def reverse_recursive(head: 'Node | None') -> 'Node | None':
    """递归反转链表，返回新头节点。"""
    raise NotImplementedError('TODO: 实现 reverse_recursive')


if __name__ == '__main__':
    original = build([1, 2, 3, 4, 5])
    print('原始    :', to_list(original))
    print('迭代反转:', to_list(reverse(build([1, 2, 3, 4, 5]))))
    print('递归反转:', to_list(reverse_recursive(build([1, 2, 3, 4, 5]))))

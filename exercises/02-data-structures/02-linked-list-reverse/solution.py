# -*- coding: utf-8 -*-
"""02 · 单链表反转

自己先写一版，然后把这里替换掉。
卡住了就 `git checkout -- exercises/02-data-structures/02-linked-list-reverse/solution.py` 回到参考实现。
"""


class Node:
    """单向链表节点。"""

    __slots__ = ("value", "next")

    def __init__(self, value, next: "Node | None" = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.value!r})"


def build(values: list) -> "Node | None":
    """把列表串成链表，返回头节点。"""
    head = None
    for value in reversed(values):
        head = Node(value, head)
    return head


def to_list(head: "Node | None") -> list:
    """把链表转回列表；检测到环则报错。"""
    result = []
    seen = 0
    cur = head
    while cur is not None:
        result.append(cur.value)
        cur = cur.next
        seen += 1
        if seen > 1_000_000:
            raise ValueError("链表存在环，to_list 无法终止")
    return result


def reverse(head: "Node | None") -> "Node | None":
    """原地反转链表，返回新头节点。O(n) 时间、O(1) 额外空间。"""
    prev = None
    cur = head
    while cur is not None:
        nxt = cur.next   # 1. 先存下一个，否则链会断
        cur.next = prev  # 2. 掉头
        prev = cur       # 3. 前移
        cur = nxt
    return prev


def reverse_recursive(head: "Node | None") -> "Node | None":
    """递归反转链表，返回新头节点。"""
    if head is None or head.next is None:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


if __name__ == "__main__":
    original = build([1, 2, 3, 4, 5])
    print("原始    :", to_list(original))
    print("迭代反转:", to_list(reverse(build([1, 2, 3, 4, 5]))))
    print("递归反转:", to_list(reverse_recursive(build([1, 2, 3, 4, 5]))))

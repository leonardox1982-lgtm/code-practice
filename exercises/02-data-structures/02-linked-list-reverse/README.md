# 02 · 单链表反转

**赛道**：02-data-structures
**考点**：链表的节点/指针模型、三指针原地反转、递归

## 题目

给定一个单向链表的节点定义（已写好，你只需实现函数）：

```python
class Node:
    __slots__ = ("value", "next")
    def __init__(self, value, next=None): ...
```

实现：

1. `build(values: list) -> Node | None`
   - 按顺序把 `values` 串成链表，返回头节点；空列表返回 `None`。

2. `to_list(head: Node | None) -> list`
   - 把链表转回 Python 列表；空链表返回 `[]`。
   - **建议加一个防护**：如果检测到环（走了超过某个上限步数），抛 `ValueError`，否则调试死循环很痛苦。

3. `reverse(head: Node | None) -> Node | None`
   - **原地**反转，返回新的头节点。
   - 要求 O(n) 时间、O(1) 额外空间（即不许先把值抄到列表再重建）。

4. `reverse_recursive(head: Node | None) -> Node | None`
   - 用递归实现同样功能，体会两种写法的差别。

## 示例

```python
>>> head = build([1, 2, 3, 4])
>>> to_list(reverse(head))
[4, 3, 2, 1]
>>> to_list(reverse(None))
[]
```

## 提示

- 迭代反转的三指针套路，用一句话记：**「先存下一个 → 掉头 → 整体前移」**。

  ```python
  prev = None
  while cur:
      nxt = cur.next   # 1. 先把下一个存下来（否则链会断）
      cur.next = prev  # 2. 掉头
      prev = cur       # 3. 前移
      cur = nxt
  return prev          # 循环结束时 prev 是新头
  ```

- 递归版的关键是**递归返回的永远是新头**，而 `head.next` 在回溯时已经变成了尾节点：

  ```python
  new_head = reverse_recursive(head.next)
  head.next.next = head
  head.next = None
  return new_head
  ```

- 别忘终止条件：`head is None or head.next is None`。

## 验收标准

- [ ] `python -m unittest -v` 全部通过
- [ ] `reverse` 不允许使用列表中转（自己检查一下代码）
- [ ] 空链表、单节点链表都要覆盖

## 参考

LeetCode 206. Reverse Linked List

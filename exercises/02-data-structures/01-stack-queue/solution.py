# -*- coding: utf-8 -*-
"""01 · 栈与队列

自己先写一版，然后把这里替换掉。
卡住了就 `git checkout -- exercises/02-data-structures/01-stack-queue/solution.py` 回到参考实现。
"""

from collections import deque

_PAIRS = {")": "(", "]": "[", "}": "{"}
_OPENERS = set(_PAIRS.values())


class Stack:
    """后进先出（LIFO）。底层用 list，append / pop 都是 O(1)。"""

    def __init__(self) -> None:
        self._data: list = []

    def push(self, item):
        self._data.append(item)
        return self

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        return not self._data

    def to_list(self) -> list:
        """从栈底到栈顶。"""
        return list(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Stack({self._data!r})"


class Queue:
    """先进先出（FIFO）。底层用 deque，避免 list.pop(0) 的 O(n)。"""

    def __init__(self) -> None:
        self._data: deque = deque()

    def enqueue(self, item):
        self._data.append(item)
        return self

    def dequeue(self):
        if not self._data:
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self):
        if not self._data:
            raise IndexError("peek from empty queue")
        return self._data[0]

    def is_empty(self) -> bool:
        return not self._data

    def to_list(self) -> list:
        """从队首到队尾。"""
        return list(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Queue({list(self._data)!r})"


def is_balanced(text: str) -> bool:
    """判断 ( ) [ ] { } 是否严格配对，其他字符忽略。"""
    stack = Stack()
    for ch in text:
        if ch in _OPENERS:
            stack.push(ch)
        elif ch in _PAIRS:
            if stack.is_empty() or stack.pop() != _PAIRS[ch]:
                return False
    return stack.is_empty()


if __name__ == "__main__":
    s = Stack()
    s.push(1).push(2).push(3)
    print(s, "-> pop:", s.pop(), "->", s)

    q = Queue()
    q.enqueue("a").enqueue("b")
    print(q, "-> dequeue:", q.dequeue(), "->", q)

    for text in ("a(b[c]{d})e", "([)]", "((", "", ")"):
        print(f"{is_balanced(text)!s:>5}  {text!r}")

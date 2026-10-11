# -*- coding: utf-8 -*-
"""01 · 栈与队列

【你的作答区】把下面的函数体补全，然后在本目录跑：

    python -m unittest -v

- 题面：同目录的 README.md
- 对答案（不改动文件）：python tools/reference.py show 01-stack-queue
- 从零重来：python tools/reference.py blank 01-stack-queue
- 还原参考实现：python tools/reference.py restore 01-stack-queue
"""
from collections import deque
_PAIRS = {')': '(', ']': '[', '}': '{'}
_OPENERS = set(_PAIRS.values())


class Stack:
    """后进先出（LIFO）。底层用 list，append / pop 都是 O(1)。"""

    def __init__(self) -> None:
        raise NotImplementedError('TODO: 实现 __init__')

    def push(self, item):
        raise NotImplementedError('TODO: 实现 push')

    def pop(self):
        raise NotImplementedError('TODO: 实现 pop')

    def peek(self):
        raise NotImplementedError('TODO: 实现 peek')

    def is_empty(self) -> bool:
        raise NotImplementedError('TODO: 实现 is_empty')

    def to_list(self) -> list:
        """从栈底到栈顶。"""
        raise NotImplementedError('TODO: 实现 to_list')

    def __len__(self) -> int:
        raise NotImplementedError('TODO: 实现 __len__')

    def __repr__(self) -> str:
        raise NotImplementedError('TODO: 实现 __repr__')


class Queue:
    """先进先出（FIFO）。底层用 deque，避免 list.pop(0) 的 O(n)。"""

    def __init__(self) -> None:
        raise NotImplementedError('TODO: 实现 __init__')

    def enqueue(self, item):
        raise NotImplementedError('TODO: 实现 enqueue')

    def dequeue(self):
        raise NotImplementedError('TODO: 实现 dequeue')

    def peek(self):
        raise NotImplementedError('TODO: 实现 peek')

    def is_empty(self) -> bool:
        raise NotImplementedError('TODO: 实现 is_empty')

    def to_list(self) -> list:
        """从队首到队尾。"""
        raise NotImplementedError('TODO: 实现 to_list')

    def __len__(self) -> int:
        raise NotImplementedError('TODO: 实现 __len__')

    def __repr__(self) -> str:
        raise NotImplementedError('TODO: 实现 __repr__')


def is_balanced(text: str) -> bool:
    """判断 ( ) [ ] { } 是否严格配对，其他字符忽略。"""
    raise NotImplementedError('TODO: 实现 is_balanced')


if __name__ == '__main__':
    s = Stack()
    s.push(1).push(2).push(3)
    print(s, '-> pop:', s.pop(), '->', s)
    q = Queue()
    q.enqueue('a').enqueue('b')
    print(q, '-> dequeue:', q.dequeue(), '->', q)
    for text in ('a(b[c]{d})e', '([)]', '((', '', ')'):
        print(f'{is_balanced(text)!s:>5}  {text!r}')

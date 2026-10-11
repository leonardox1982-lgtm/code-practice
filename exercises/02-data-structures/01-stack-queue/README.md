# 01 · 栈与队列

**赛道**：02-data-structures
**考点**：LIFO / FIFO 语义、`list` 与 `collections.deque` 的选择、异常约定

## 题目

### 第一部分：实现两个容器

**`Stack`（栈，后进先出）**

| 方法 | 行为 |
| --- | --- |
| `push(item)` | 压栈，返回 `self`（方便链式调用） |
| `pop()` | 弹出并返回栈顶元素；空栈抛 `IndexError` |
| `peek()` | 返回栈顶元素但不弹出；空栈抛 `IndexError` |
| `is_empty()` | 是否为空 |
| `__len__()` | 元素个数 |
| `to_list()` | 返回从**栈底到栈顶**的列表 |

**`Queue`（队列，先进先出）**

| 方法 | 行为 |
| --- | --- |
| `enqueue(item)` | 入队，返回 `self` |
| `dequeue()` | 出队并返回队首元素；空队列抛 `IndexError` |
| `peek()` | 返回队首元素但不移除；空队列抛 `IndexError` |
| `is_empty()` / `__len__()` / `to_list()` | 同上；`to_list()` 从**队首到队尾** |

用 `repr(stack)` 能看到内容更方便调试，建议实现 `__repr__`。

### 第二部分：用栈解决一个真问题

`is_balanced(text: str) -> bool`

判断括号是否配对。只关心 `()`、`[]`、`{}` 三种括号对，其他字符一律忽略。

## 示例

```python
>>> s = Stack()
>>> s.push(1).push(2).push(3)
>>> s.pop()
3
>>> s.to_list()
[1, 2]
>>> q = Queue()
>>> q.enqueue("a").enqueue("b")
>>> q.dequeue()
'a'
>>> is_balanced("a(b[c]{d})e")
True
>>> is_balanced("([)]")
False
```

## 提示

- 栈用 `list` 就够：`append` / `pop` 都是 O(1)。
- **队列别用 `list`**：`list.pop(0)` 是 O(n)，元素多了会明显变慢。用 `collections.deque` 的 `popleft()`，O(1)。
- `is_balanced` 的套路：遇到左括号压栈；遇到右括号就弹栈，看弹出的左括号是否和它配对；弹不出来（栈空）说明右括号多余。**全部扫完还要检查栈是否为空**，否则 `"(("` 会被误判成 `True`。
- 建立一个映射 `{")": "(", "]": "[", "}": "{"}`，配对判断写起来最干净。

## 验收标准

- [ ] `python -m unittest -v` 全部通过
- [ ] 空栈 `pop()` / `peek()` 抛的是 `IndexError`
- [ ] `is_balanced("((")` 返回 `False`（这是最容易漏的用例）

## 参考

《算法（第 4 版）》1.3 节 背包、队列和栈；LeetCode 20. Valid Parentheses

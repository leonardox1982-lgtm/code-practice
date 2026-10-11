# 03 · 词频统计

**赛道**：01-python-basics
**考点**：正则表达式、`collections.Counter`、多级排序、字典

## 题目

实现两个函数：

1. `word_count(text: str) -> dict[str, int]`
   - 从 `text` 中提取**英文单词**（以字母开头，后面可以跟字母或撇号，例如 `it's`、`don't`）；
   - 统一转小写；
   - 返回「单词 → 出现次数」的字典。

2. `top_n(text: str, n: int = 3) -> list[tuple[str, int]]`
   - 返回出现次数最多的前 `n` 个词，形如 `[("the", 5), ("a", 3)]`；
   - **次数相同则按单词升序排列**（保证结果稳定、可测试）；
   - `n <= 0` 返回空列表。

## 示例

```python
>>> word_count("The cat and the hat.")
{'the': 2, 'cat': 1, 'and': 1, 'hat': 1}
>>> top_n("b a b c a b", 2)
[('b', 3), ('a', 2)]
```

## 提示

- 用 `re.findall(r"[A-Za-z][A-Za-z']*", text)` 抓单词，比 `text.split()` 稳（能处理标点）。
- `Counter` 的构造可以直接吃一个生成器：`Counter(w.lower() for w in words)`。
- 排序用 `sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))`。**负号用来把「降序」和「升序」写进同一个 key**，这是很常用的技巧。
- 中文不在本题要求内，但你可以加一个「按单字切分」的扩展自己玩。

## 验收标准

- [ ] `python -m unittest -v` 全部通过
- [ ] 标点不会污染单词（`"hat."` 要算成 `hat`）
- [ ] `top_n` 在次数相同时结果稳定

## 参考

经典文本处理练习；`Counter.most_common()` 也是标准答案，但请自己写排序，顺手练 `key=`。

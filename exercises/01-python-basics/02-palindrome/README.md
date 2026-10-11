# 02 · 回文判断

**赛道**：01-python-basics
**考点**：字符串清洗、切片反转、Unicode 处理、生成器表达式

## 题目

实现两个函数：

1. `normalize(text: str) -> str`
   - 只保留**字母和数字**（用 `str.isalnum()` 判断），其余字符（空格、标点、下划线等）全部丢弃；
   - 全部转成小写。

2. `is_palindrome(text: str) -> bool`
   - 先 `normalize`，再判断是否正读反读一致；
   - 空串或清洗后为空 → `True`。

## 示例

```python
>>> normalize("A man, a plan, a canal: Panama")
'amanaplanacanalpanama'
>>> is_palindrome("A man, a plan, a canal: Panama")
True
>>> is_palindrome("race a car")
False
>>> is_palindrome("上海自来水来自海上")
True
```

## 提示

- 反转字符串最简洁的写法是切片：`s[::-1]`。
- `str.isalnum()` 对中文、日文等 Unicode 字母同样返回 `True`，所以上面的中文例子能直接过。
- 用 `"".join(...)` 把生成器表达式拼成字符串，比反复 `+=` 高效得多。
- 想省内存可以用双指针（`i` 从头、`j` 从尾往中间夹），但注意别把复杂度写坏。

## 验收标准

- [ ] `python -m unittest -v` 全部通过
- [ ] 大小写混排、标点混排都能正确判定
- [ ] 中文回文能正确判定

## 参考

LeetCode 125. Valid Palindrome

# 01 · FizzBuzz

**赛道**：01-python-basics
**考点**：条件分支的先后顺序、取模运算、列表推导

## 题目

实现两个函数：

1. `fizzbuzz(n: int) -> str`
   - `n` 同时是 3 和 5 的倍数 → `"FizzBuzz"`
   - `n` 是 3 的倍数 → `"Fizz"`
   - `n` 是 5 的倍数 → `"Buzz"`
   - 其余 → `n` 的十进制字符串

2. `fizzbuzz_list(n: int) -> list[str]`
   - 返回从 **1** 到 `n`（含 `n`）的序列；`n <= 0` 时返回空列表。

## 示例

```python
>>> fizzbuzz(3)
'Fizz'
>>> fizzbuzz(15)
'FizzBuzz'
>>> fizzbuzz(7)
'7'
>>> fizzbuzz_list(15)[-1]
'FizzBuzz'
```

## 提示

- 判断顺序很关键：如果先判 `n % 3 == 0`，15 会被错判成 `"Fizz"`。所以 **15 的判断必须排在 3 和 5 前面**。
- 另一种写法是先取两个布尔值再拼字符串，可以避免顺序问题：
  `("Fizz" if n % 3 == 0 else "") + ("Buzz" if n % 5 == 0 else "")`。
- `range(1, n + 1)` 才能拿到 1..n。

## 验收标准

- [ ] `python -m unittest -v` 全部通过
- [ ] `fizzbuzz_list(0)` 返回 `[]`，不是 `[""]`

## 参考

经典面试题，常见于《Cracking the Coding Interview》。

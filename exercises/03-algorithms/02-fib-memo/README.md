# 02 · 斐波那契的三种写法

**赛道**：03-algorithms
**考点**：递归树、记忆化、迭代、复杂度直觉

## 题目

约定 `fib(0) = 0`、`fib(1) = 1`、`fib(n) = fib(n-1) + fib(n-2)`。

实现四个函数：

1. `fib_recursive(n: int) -> int`
   - 最朴素的递归，**不加任何缓存**。只为理解递归树，n 大了会很慢。

2. `fib_memo(n: int) -> int`
   - 记忆化递归。可以用 `functools.lru_cache`，也可以自己维护字典。

3. `fib_iter(n: int) -> int`
   - 迭代，只用两个变量滚动。要求能秒算 `fib_iter(1000)`。

4. `fib_list(n: int) -> list[int]`
   - 返回前 `n` 项 `[F(0), F(1), ..., F(n-1)]`；`n <= 0` 返回 `[]`。

负数 `n` 一律抛 `ValueError`。

## 示例

```python
>>> fib_recursive(10)
55
>>> fib_memo(100)
354224848179261915075
>>> fib_iter(10)
55
>>> fib_list(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## 提示

- 朴素递归慢在哪：算 `fib(5)` 要算两遍 `fib(3)`、三遍 `fib(2)`……**调用次数本身也是斐波那契数列**，所以是 O(φⁿ) 的指数级。
- 记忆化就是用空间换时间：把算过的 `fib(k)` 存起来，之后 O(1) 取。
  `lru_cache` 版本只需要三行：

  ```python
  from functools import lru_cache

  @lru_cache(maxsize=None)
  def fib_memo(n):
      if n < 2:
          return n
      return fib_memo(n - 1) + fib_memo(n - 2)
  ```

- 迭代版注意边界：`n < 2` 直接返回 `n`；循环从 `2` 到 `n`。
- Python 整数是任意精度的，`fib_iter(1000)` 有 209 位数字，算起来毫无压力——顺手体会一下「大整数」和 C 语言的区别。

## 验收标准

- [ ] `python -m unittest -v` 全部通过
- [ ] `fib_memo(100)` / `fib_iter(100)` 结果一致
- [ ] `fib_recursive` 只在小 n 上被测（测试里会用调用计数证明它确实是指数级）

## 参考

MIT 6.042J Ch.5 Induction（用归纳法证明斐波那契恒等式）

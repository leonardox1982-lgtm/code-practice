# 02 · 欧几里得算法与模逆元

**赛道**：04-discrete-math
**考点**：辗转相除、贝祖等式、扩展欧几里得、模运算

> 对应 MIT 6.042J **第 8 章 Number Theory**。教材用「良序原理 + 辗转相除」证明 `gcd(a, b) = gcd(b, a mod b)`，这道题把证明变成代码。

## 题目

1. `gcd(a: int, b: int) -> int`
   - 最大公约数，**结果非负**：`gcd(-4, 6) == 2`，`gcd(0, 0) == 0`。

2. `lcm(a: int, b: int) -> int`
   - 最小公倍数，结果非负；任一方为 0 时返回 `0`。
   - 提示：`lcm(a, b) = |a * b| // gcd(a, b)`。**先除后乘**可以少一次大数运算。

3. `extended_gcd(a: int, b: int) -> tuple[int, int, int]`
   - 返回 `(g, x, y)`，满足 **`a*x + b*y == g`**（贝祖等式），其中 `g == gcd(a, b)`。

4. `mod_inverse(a: int, m: int) -> int`
   - 返回 `a` 在模 `m` 下的乘法逆元 `x`，满足 `(a * x) % m == 1`，且 `0 <= x < m`；
   - 若逆元不存在（即 `gcd(a, m) != 1`）抛 `ValueError`；
   - `m <= 1` 抛 `ValueError`。

## 示例

```python
>>> gcd(1071, 462)
21
>>> lcm(4, 6)
12
>>> extended_gcd(240, 46)
(2, -9, 47)          # 240 × (-9) + 46 × 47 = 2
>>> mod_inverse(3, 11)
4
>>> (3 * 4) % 11
1
```

## 提示

`extended_gcd` 的递归写法极短，回溯时把系数「转一下」即可：

```python
def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = extended_gcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)
```

为什么对？设 `g = b*x1 + (a mod b)*y1`，把 `a mod b = a - (a//b)*b` 代进去整理，
就得到 `g = a*y1 + b*(x1 - (a//b)*y1)` —— 正好是返回的 `(g, y1, x1 - (a//b)*y1)`。

处理负数的小技巧：**先对绝对值算，再按符号把系数反号**：

```python
g, x, y = extended_gcd(abs(a), abs(b))
return (g, -x if a < 0 else x, -y if b < 0 else y)
```

`mod_inverse` 就是 `extended_gcd` 的直接应用：先拿到 `a*x + m*y = g`，
若 `g != 1` 则无解；否则 `a*x ≡ 1 (mod m)`，取 `x % m` 就是答案。

## 验收标准

- [ ] `python -m unittest -v` 全部通过
- [ ] `extended_gcd` 的返回值必须真的满足 `a*x + b*y == g`（测试会用随机大数校验）
- [ ] `gcd` / `lcm` 对负数、零都不崩
- [ ] `mod_inverse` 在 `gcd(a, m) != 1` 时抛 `ValueError`

## 参考

MIT 6.042J Ch.8.2–8.4；《具体数学》第 4 章（数论）

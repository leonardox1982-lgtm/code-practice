# 01 · 素数筛与质因数分解

**赛道**：04-discrete-math
**考点**：埃拉托斯特尼筛、试除判素、算术基本定理

> 对应 MIT 6.042J **第 8 章 Number Theory**。教材里证明了「每个大于 1 的整数都能唯一分解为素数乘积」（算术基本定理），这道题就是把它写成代码。

## 题目

1. `sieve(limit: int) -> list[int]`
   - 返回 `[2, limit]` 区间内所有素数，升序。
   - 要求 O(n log log n)：用筛法，**不要**对每个数单独试除。
   - `limit < 2` 返回 `[]`。

2. `is_prime(n: int) -> bool`
   - 单独判断一个数是否素数。
   - 试除只需要做到 √n；可以用 `6k ± 1` 的轮子提速（大于 3 的素数必然形如 6k±1）。
   - `n < 2` 返回 `False`。

3. `prime_factors(n: int) -> list[int]`
   - 返回 `n` 的质因数（**带重数**），升序。
   - 例如 `12 -> [2, 2, 3]`；`n < 2` 返回 `[]`。
   - 负数抛 `ValueError`。

4. `count_primes(limit: int) -> int`
   - 即 π(limit)，用筛法的结果数个数。

## 示例

```python
>>> sieve(30)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> is_prime(97)
True
>>> is_prime(91)          # 91 = 7 × 13
False
>>> prime_factors(360)    # 360 = 2³ × 3² × 5
[2, 2, 2, 3, 3, 5]
>>> count_primes(1_000_000)
78498
```

## 提示

筛法的骨架，用 `bytearray` 当标记数组最省内存：

```python
def sieve(limit):
    if limit < 2:
        return []
    flags = bytearray([1]) * (limit + 1)
    flags[0] = flags[1] = 0
    for p in range(2, int(limit ** 0.5) + 1):
        if flags[p]:
            flags[p * p::p] = b"\x00" * len(flags[p * p::p])   # 从 p² 开始划掉
    return [i for i in range(2, limit + 1) if flags[i]]
```

两个关键点：

- **内层从 `p*p` 开始划**，因为比 `p²` 小的 `p` 的倍数早被更小的素数划过了。这一条直接决定了复杂度是不是 O(n log log n)。
- 外层只需要到 `√limit`，再大的素数其平方已经超出范围。

`prime_factors` 的思路是「从小到大不停地除」：

```python
d = 2
while d * d <= n:
    while n % d == 0:
        out.append(d)
        n //= d
    d += 1
if n > 1:      # 剩下的是最后一个大素数，别漏
    out.append(n)
```

## 验收标准

- [ ] `python -m unittest -v` 全部通过
- [ ] `sieve(1_000_000)` 能秒出，结果个数为 78498
- [ ] `is_prime` 与 `sieve` 在两两之间结果一致（测试里会用 ≤ 2000 的区间对拍）
- [ ] `prime_factors` 的乘积必须等于原数（随机对拍）

## 参考

MIT 6.042J Ch.8；《编程珠玑》第 1 章（筛法与位图）

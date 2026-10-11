# -*- coding: utf-8 -*-
"""02 · 欧几里得算法与模逆元

自己先写一版，然后把这里替换掉。
卡住了就 `git checkout -- exercises/04-discrete-math/02-gcd-euclid/solution.py` 回到参考实现。
"""


def gcd(a: int, b: int) -> int:
    """最大公约数，结果非负。gcd(0, 0) == 0。"""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """最小公倍数，结果非负；任一方为 0 时返回 0。"""
    a, b = abs(a), abs(b)
    if a == 0 or b == 0:
        return 0
    return a // gcd(a, b) * b        # 先除后乘，避免中间结果过大


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """返回 (g, x, y) 使得 a*x + b*y == g，其中 g == gcd(a, b)。"""
    g, x, y = _extended_gcd_positive(abs(a), abs(b))
    return (g, -x if a < 0 else x, -y if b < 0 else y)


def _extended_gcd_positive(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = _extended_gcd_positive(b, a % b)
    return (g, y1, x1 - (a // b) * y1)


def mod_inverse(a: int, m: int) -> int:
    """a 在模 m 下的乘法逆元；不存在时抛 ValueError。"""
    if m <= 1:
        raise ValueError("m must be greater than 1")
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"{a} 在模 {m} 下没有逆元（gcd = {g}）")
    return x % m


if __name__ == "__main__":
    print("gcd(1071, 462) =", gcd(1071, 462))
    print("lcm(4, 6)      =", lcm(4, 6))
    g, x, y = extended_gcd(240, 46)
    print(f"extended_gcd(240, 46) = {(g, x, y)}  "
          f"校验: 240*{x} + 46*{y} = {240 * x + 46 * y}")
    print("mod_inverse(3, 11) =", mod_inverse(3, 11))
    for m in (4, 6, 8):
        try:
            mod_inverse(2, m)
        except ValueError as exc:
            print(f"  mod_inverse(2, {m}) -> {exc}")

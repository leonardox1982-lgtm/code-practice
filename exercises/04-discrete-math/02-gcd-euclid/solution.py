# -*- coding: utf-8 -*-
"""02 · 欧几里得算法与模逆元

【你的作答区】把下面的函数体补全，然后在本目录跑：

    python -m unittest -v

- 题面：同目录的 README.md
- 对答案（不改动文件）：python tools/reference.py show 02-gcd-euclid
- 从零重来：python tools/reference.py blank 02-gcd-euclid
- 还原参考实现：python tools/reference.py restore 02-gcd-euclid
"""


def gcd(a: int, b: int) -> int:
    """最大公约数，结果非负。gcd(0, 0) == 0。"""
    raise NotImplementedError('TODO: 实现 gcd')


def lcm(a: int, b: int) -> int:
    """最小公倍数，结果非负；任一方为 0 时返回 0。"""
    raise NotImplementedError('TODO: 实现 lcm')


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """返回 (g, x, y) 使得 a*x + b*y == g，其中 g == gcd(a, b)。"""
    raise NotImplementedError('TODO: 实现 extended_gcd')


def _extended_gcd_positive(a: int, b: int) -> tuple[int, int, int]:
    raise NotImplementedError('TODO: 实现 _extended_gcd_positive')


def mod_inverse(a: int, m: int) -> int:
    """a 在模 m 下的乘法逆元；不存在时抛 ValueError。"""
    raise NotImplementedError('TODO: 实现 mod_inverse')


if __name__ == '__main__':
    print('gcd(1071, 462) =', gcd(1071, 462))
    print('lcm(4, 6)      =', lcm(4, 6))
    g, x, y = extended_gcd(240, 46)
    print(f'extended_gcd(240, 46) = {(g, x, y)}  校验: 240*{x} + 46*{y} = {240 * x + 46 * y}')
    print('mod_inverse(3, 11) =', mod_inverse(3, 11))
    for m in (4, 6, 8):
        try:
            mod_inverse(2, m)
        except ValueError as exc:
            print(f'  mod_inverse(2, {m}) -> {exc}')

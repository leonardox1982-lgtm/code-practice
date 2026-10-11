# -*- coding: utf-8 -*-
"""01 · FizzBuzz

自己先写一版，然后把这里替换掉。
卡住了就 `git checkout -- exercises/01-python-basics/01-fizzbuzz/solution.py` 回到参考实现。
"""


def fizzbuzz(n: int) -> str:
    """按 FizzBuzz 规则返回 n 对应的字符串。"""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def fizzbuzz_list(n: int) -> list[str]:
    """返回 1..n 的 FizzBuzz 序列，n <= 0 时返回空列表。"""
    return [fizzbuzz(i) for i in range(1, n + 1)]


if __name__ == "__main__":
    print(" ".join(fizzbuzz_list(20)))

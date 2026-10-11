# code-practice · 代码练习仓库

[![tests](https://github.com/leonardox1982-lgtm/code-practice/actions/workflows/ci.yml/badge.svg)](https://github.com/leonardox1982-lgtm/code-practice/actions/workflows/ci.yml)

个人编程练习与学习记录。每道练习都是**可运行、可验证**的：配套单元测试会自动检查实现对不对，本地一条命令跑通，GitHub Actions 上也会自动跑。

- 仓库地址：<https://github.com/leonardox1982-lgtm/code-practice>
- 主线语言：**Python 3.13**（只用标准库，零第三方依赖）
- 支线：**JavaScript / Node 22**（用内置 `node --test`，同样零依赖）

---

## 目录结构

```
code-practice/
├── README.md                       ← 你在这里
├── exercises/                      ← 练习主体，按主题分六个赛道
│   ├── 01-python-basics/           Python 基础：条件、循环、字符串、字典
│   ├── 02-data-structures/         数据结构：栈、队列、链表、二分查找
│   ├── 03-algorithms/              算法思想：分治、动态规划、贪心
│   ├── 04-discrete-math/           离散数学（对应 MIT 6.042J 的数论部分）
│   ├── 05-data-analysis/           数据分析入门：CSV 读取与统计量
│   └── 06-web-js/                  JavaScript / Node 支线
├── .solutions/                     ← 参考答案，与 exercises/ 同构（别提前偷看）
├── notes/                          学习笔记（中文）
│   └── mit-6.042j/                 与数学课对应的笔记
├── playground/                     沙盒，随便写，不进 CI
└── tools/
    ├── run_all_tests.py            一键跑全部测试
    ├── reference.py                对答案 / 还原 / 清回骨架 / 归档答案
    └── new_exercise.py             脚手架：生成一道新练习
```

每道练习的目录都是同一套结构：

```
exercises/<赛道>/<题号-题目>/
├── README.md          题面：要求、提示、验收标准
├── solution.py        你的作答区（出厂只有函数签名和文档，没有答案）
└── test_solution.py   单元测试
```

---

## 快速开始

```bash
git clone git@github.com:leonardox1982-lgtm/code-practice.git
cd code-practice

# 跑通全部练习的测试
python tools/run_all_tests.py

# 只跑某个赛道（按路径片段过滤）
python tools/run_all_tests.py 01
python tools/run_all_tests.py 04-discrete

# 只跑单道题
cd exercises/01-python-basics/01-fizzbuzz
python -m unittest -v
```

> 本机 Python 装在 `C:\Users\Administrator\AppData\Local\Programs\Python\Python313\python.exe`，
> 若 `python` 不在 PATH 里，用完整路径代替即可。
>
> 在 VS Code 里按 `Ctrl+Shift+P` → **Tasks: Run Test Task** 也能一键跑；
> 想跑单道题就在打开该题目录的文件时用「测试：只跑当前打开的练习」。

## 怎么练

打开任何一道题，`solution.py` 出厂时都是**骨架** —— 只有函数签名、文档字符串和
`raise NotImplementedError`，不会一打开就看到答案。

```bash
cd exercises/01-python-basics/01-fizzbuzz

cat README.md                                            # 1. 读题面
#                                                        # 2. 在 solution.py 里写实现
python -m unittest -v                                    # 3. 跑测试

python ../../../tools/reference.py show 01-fizzbuzz      # 4. 对答案（不动你的文件）
python ../../../tools/reference.py restore 01-fizzbuzz   # 5. 看答案直接跑起来
python ../../../tools/reference.py blank 01-fizzbuzz     # 6. 想从零重来
```

在仓库根目录跑更省事，题号支持模糊匹配：

```bash
python tools/reference.py list              # 每道题的作答状态 + 总进度
python tools/reference.py show 01-fizz       # 打印参考答案
python tools/reference.py restore 01-fizz    # 用参考答案覆盖你的文件
python tools/reference.py blank 01-fizz      # 把你的文件清回骨架
```

> `restore` / `blank` 会覆盖你已经写的内容，所以对「已作答」的文件默认拒绝执行，
> 确认要动就加 `--force`。

测试永远只比对 `solution.py`，所以「写 → 测 → 对答案 → 重来」这个循环天然成立。

## 新增一道练习

```bash
python tools/new_exercise.py 03-algorithms 04-two-sum
```

会在 `exercises/03-algorithms/04-two-sum/` 下生成 README + solution 骨架 + 测试骨架。
写完照着 `README.md` 里的验收标准把测试补全即可。

参考实现写好后归档进 `.solutions/`，原文件会自动清成骨架：

```bash
python tools/reference.py save 03-algorithms/04-two-sum
```

---

## 关于 `.solutions/` 与 CI

- `.solutions/` 与 `exercises/` 目录结构一一对应，存放每道题的**参考答案**。
- CI 会先把参考答案铺回 `exercises/` 再跑测试 —— 它验证的是**题目与参考答案是否自洽**，
  跟你本地做到哪一题无关。
- 所以你提交自己的作答后 CI 依然会绿（它跑的不是你的代码）。
  自己的实现过没过，以本地 `python tools/run_all_tests.py` 为准。

---

## 练习清单

### 01 · Python 基础

| 题目 | 考点 |
| --- | --- |
| [01-fizzbuzz](exercises/01-python-basics/01-fizzbuzz) | 条件分支、取模、列表推导 |
| [02-palindrome](exercises/01-python-basics/02-palindrome) | 字符串清洗、切片反转、Unicode |
| [03-word-count](exercises/01-python-basics/03-word-count) | 正则、`collections.Counter`、多级排序 |

### 02 · 数据结构

| 题目 | 考点 |
| --- | --- |
| [01-stack-queue](exercises/02-data-structures/01-stack-queue) | 用 `list` / `deque` 实现栈与队列 |
| [02-linked-list-reverse](exercises/02-data-structures/02-linked-list-reverse) | 单链表、三指针原地反转 |
| [03-binary-search](exercises/02-data-structures/03-binary-search) | 二分查找、边界（`lower_bound`） |

### 03 · 算法思想

| 题目 | 考点 |
| --- | --- |
| [01-sorting](exercises/03-algorithms/01-sorting) | 分治：快速排序、归并排序 |
| [02-fib-memo](exercises/03-algorithms/02-fib-memo) | 递归 → 记忆化 → 迭代，复杂度对比 |
| [03-max-subarray](exercises/03-algorithms/03-max-subarray) | 动态规划 / Kadane 算法 |

### 04 · 离散数学（对应 MIT 6.042J）

| 题目 | 考点 |
| --- | --- |
| [01-sieve-prime](exercises/04-discrete-math/01-sieve-prime) | 埃拉托斯特尼筛、试除判素、质因数分解 |
| [02-gcd-euclid](exercises/04-discrete-math/02-gcd-euclid) | 欧几里得算法、扩展欧几里得、模逆元 |

### 05 · 数据分析

| 题目 | 考点 |
| --- | --- |
| [01-csv-stats](exercises/05-data-analysis/01-csv-stats) | `csv` 模块、均值/中位数/标准差 |

### 06 · JavaScript

| 题目 | 考点 |
| --- | --- |
| [01-array-utils](exercises/06-web-js/01-array-utils) | ES Module、`node:test`、数组高阶方法 |

---

## 环境

| 组件 | 版本 | 说明 |
| --- | --- | --- |
| Python | 3.13 | 全部 Python 练习与测试只依赖标准库 |
| Node.js | 22+ | 只有 `06-web-js` 赛道需要 |

不需要 `pip install` 任何东西，测试用的是内置 `unittest`。

## 提交习惯

```bash
git add -A
git commit -m "feat(01-python-basics): 完成 fizzbuzz"
git push
```

提交信息用 Conventional Commits 的简化版即可：`feat` / `fix` / `docs` / `chore`。

## 许可

MIT，见 [LICENSE](LICENSE)。

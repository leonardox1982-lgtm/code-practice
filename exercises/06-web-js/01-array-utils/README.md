# 01 · 数组工具集

**赛道**：06-web-js
**考点**：ES Module、`node:test` 内置测试运行器、`Set` / `reduce` / `??=`、不可变风格

## 题目

在 `array-utils.mjs` 里实现并导出六个函数。**全部返回新数组/新对象，不修改入参。**

| 函数 | 要求 |
| --- | --- |
| `unique(values)` | 保序去重，基于 `Set`，O(n) |
| `chunk(values, size)` | 按 `size` 切块，最后一块可不满；`size` 非正整数抛 `RangeError` |
| `groupBy(values, keyFn)` | 按 `keyFn(value, index)` 的返回值分组，得到 `{ key: [items] }` |
| `flatten(values, depth)` | 扁平化到指定深度，默认无限深；`depth = 0` 原样返回 |
| `sum(values)` | 求和，空数组返回 `0` |
| `countBy(values, keyFn)` | 分组计数，得到 `{ key: 次数 }` |

## 示例

```js
import { chunk, unique, groupBy } from './array-utils.mjs';

unique([3, 1, 3, 2]);                  // [3, 1, 2]
chunk([1, 2, 3, 4, 5], 2);             // [[1,2], [3,4], [5]]
groupBy(['a', 'bb', 'cc'], s => s.length);
// { 1: ['a'], 2: ['bb', 'cc'] }
```

## 提示

- 去重最快的就是一行：`[...new Set(values)]`。**`Set` 用 SameValueZero 判等**，所以 `1` 和 `'1'` 是两个不同的值。
- 切块用 `slice` 逐段取，比 `splice` 安全（`splice` 会改原数组）：

  ```js
  for (let i = 0; i < values.length; i += size) out.push(values.slice(i, i + size));
  ```

- `out[key] ??= []` 是「为空或 undefined 时才赋值」的简写，等价于
  `out[key] = out[key] ?? []`。用它分组非常顺。
- `flatten` 的递归版本里，**`Infinity - 1` 还是 `Infinity`**，所以默认深度不用特殊处理：

  ```js
  export function flatten(values, depth = Infinity) {
    if (depth <= 0) return values.slice();
    const out = [];
    for (const v of values) {
      if (Array.isArray(v)) out.push(...flatten(v, depth - 1));
      else out.push(v);
    }
    return out;
  }
  ```

- ⚠️ 顺手记一个坑：`sum([0.1, 0.2])` **不等于** `0.3`，而是 `0.30000000000000004`。这是 IEEE 754 双精度的固有问题，测试里专门留了一个用例点出来。
- 注意不要用 `Array.prototype.flat` 直接实现 `flatten`——那这题就没意义了。想偷懒可以，但先自己写一遍。

## 验收标准

- [ ] `node --test` 全部通过
- [ ] 非法 `size` 抛的是 `RangeError`，不是 `Error`
- [ ] 所有函数都不修改入参（测试里有专门用例）

## 跑测试

```bash
cd exercises/06-web-js/01-array-utils
node --test            # 或者 npm test
```

## 参考

MDN: `Set`、`Array.prototype.reduce`、`Nullish coalescing assignment (??=)`

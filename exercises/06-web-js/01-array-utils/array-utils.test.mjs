/**
 * 数组工具集的单元测试 —— 用 Node 内置测试运行器，零依赖。
 *
 * 跑测试：在本目录下执行 `node --test`
 */

import test from 'node:test';
import assert from 'node:assert/strict';

import { chunk, countBy, flatten, groupBy, sum, unique } from './array-utils.mjs';

test('unique: 保序去重', () => {
  assert.deepEqual(unique([3, 1, 3, 2, 1]), [3, 1, 2]);
  assert.deepEqual(unique([]), []);
  assert.deepEqual(unique(['a', 'a']), ['a']);
  assert.deepEqual(unique([1, '1']), [1, '1']); // Set 区分类型
});

test('unique: 不修改入参', () => {
  const input = [1, 1, 2];
  unique(input);
  assert.deepEqual(input, [1, 1, 2]);
});

test('chunk: 基本切分', () => {
  assert.deepEqual(chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]]);
  assert.deepEqual(chunk([1, 2, 3, 4], 2), [[1, 2], [3, 4]]);
  assert.deepEqual(chunk([], 3), []);
  assert.deepEqual(chunk([1], 5), [[1]]);
});

test('chunk: 非法 size 抛 RangeError', () => {
  for (const bad of [0, -1, 1.5, NaN]) {
    assert.throws(() => chunk([1, 2], bad), RangeError);
  }
});

test('groupBy: 按字符串键分组', () => {
  const people = [
    { name: '阿明', dept: '研发' },
    { name: '小美', dept: '运营' },
    { name: '老张', dept: '研发' },
  ];
  assert.deepEqual(groupBy(people, (p) => p.dept), {
    研发: [people[0], people[2]],
    运营: [people[1]],
  });
});

test('groupBy: keyFn 能拿到下标', () => {
  assert.deepEqual(groupBy(['a', 'b', 'c', 'd'], (_v, i) => (i % 2 === 0 ? 'even' : 'odd')), {
    even: ['a', 'c'],
    odd: ['b', 'd'],
  });
});

test('groupBy: 空数组返回空对象', () => {
  assert.deepEqual(groupBy([], (v) => v), {});
});

test('flatten: 无限深度（默认）', () => {
  assert.deepEqual(flatten([1, [2, [3, [4]]]]), [1, 2, 3, 4]);
  assert.deepEqual(flatten([]), []);
  assert.deepEqual(flatten([1, 2]), [1, 2]);
});

test('flatten: 限定深度', () => {
  assert.deepEqual(flatten([1, [2, [3, [4]]]], 1), [1, 2, [3, [4]]]);
  assert.deepEqual(flatten([1, [2, [3, [4]]]], 2), [1, 2, 3, [4]]);
  assert.deepEqual(flatten([1, [2]], 0), [1, [2]]);
});

test('sum: 求和与边界', () => {
  assert.equal(sum([1, 2, 3]), 6);
  assert.equal(sum([]), 0);
  assert.equal(sum([-1, 1]), 0);
  assert.equal(sum([0.1, 0.2]), 0.30000000000000004); // 浮点就是这么回事
});

test('countBy: 分组计数', () => {
  assert.deepEqual(countBy(['a', 'b', 'a', 'a'], (v) => v), { a: 3, b: 1 });
  assert.deepEqual(countBy([], (v) => v), {});
  assert.deepEqual(countBy([1, 2, 3, 4], (v) => (v % 2 ? 'odd' : 'even')), { odd: 2, even: 2 });
});

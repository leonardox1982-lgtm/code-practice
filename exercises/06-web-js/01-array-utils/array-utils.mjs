/**
 * 数组工具集 —— ES Module 写法，零第三方依赖。
 *
 * 覆盖高频场景：去重、分块、分组、扁平化、求和。
 * 每个函数都返回新数组/新对象，不修改入参。
 */

/**
 * 保序去重。基于 Set，O(n)。
 * @param {Array} values
 * @returns {Array}
 */
export function unique(values) {
  return [...new Set(values)];
}

/**
 * 把数组按固定长度切成若干块，最后一块可以不满。
 * @param {Array} values
 * @param {number} size 正整数
 * @returns {Array<Array>}
 */
export function chunk(values, size) {
  if (!Number.isInteger(size) || size <= 0) {
    throw new RangeError(`size 必须是正整数，收到 ${size}`);
  }
  const out = [];
  for (let i = 0; i < values.length; i += size) {
    out.push(values.slice(i, i + size));
  }
  return out;
}

/**
 * 按 key 分组，key 由 keyFn(value, index) 返回。
 * @param {Array} values
 * @param {(value: any, index: number) => string} keyFn
 * @returns {Record<string, Array>}
 */
export function groupBy(values, keyFn) {
  const out = {};
  values.forEach((value, index) => {
    const key = keyFn(value, index);
    (out[key] ??= []).push(value);
  });
  return out;
}

/**
 * 扁平化到指定深度（默认无限深）。
 * @param {Array} values
 * @param {number} depth
 * @returns {Array}
 */
export function flatten(values, depth = Infinity) {
  if (depth <= 0) return values.slice();
  const out = [];
  for (const value of values) {
    if (Array.isArray(value)) {
      out.push(...flatten(value, depth - 1));
    } else {
      out.push(value);
    }
  }
  return out;
}

/**
 * 求和。空数组返回 0（也就是 reduce 的初始值）。
 * @param {number[]} values
 * @returns {number}
 */
export function sum(values) {
  return values.reduce((acc, value) => acc + value, 0);
}

/**
 * 简单分组计数，返回 { key: 出现次数 }。
 * @param {Array} values
 * @param {(value: any) => string} keyFn
 * @returns {Record<string, number>}
 */
export function countBy(values, keyFn) {
  const out = {};
  for (const value of values) {
    const key = keyFn(value);
    out[key] = (out[key] ?? 0) + 1;
  }
  return out;
}

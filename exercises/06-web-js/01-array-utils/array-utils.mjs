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
  throw new Error('TODO: 实现 unique');
}

/**
 * 把数组按固定长度切成若干块，最后一块可以不满。
 * @param {Array} values
 * @param {number} size 正整数
 * @returns {Array<Array>}
 */
export function chunk(values, size) {
  throw new Error('TODO: 实现 chunk');
}

/**
 * 按 key 分组，key 由 keyFn(value, index) 返回。
 * @param {Array} values
 * @param {(value: any, index: number) => string} keyFn
 * @returns {Record<string, Array>}
 */
export function groupBy(values, keyFn) {
  throw new Error('TODO: 实现 groupBy');
}

/**
 * 扁平化到指定深度（默认无限深）。
 * @param {Array} values
 * @param {number} depth
 * @returns {Array}
 */
export function flatten(values, depth = Infinity) {
  throw new Error('TODO: 实现 flatten');
}

/**
 * 求和。空数组返回 0（也就是 reduce 的初始值）。
 * @param {number[]} values
 * @returns {number}
 */
export function sum(values) {
  throw new Error('TODO: 实现 sum');
}

/**
 * 简单分组计数，返回 { key: 出现次数 }。
 * @param {Array} values
 * @param {(value: any) => string} keyFn
 * @returns {Record<string, number>}
 */
export function countBy(values, keyFn) {
  throw new Error('TODO: 实现 countBy');
}

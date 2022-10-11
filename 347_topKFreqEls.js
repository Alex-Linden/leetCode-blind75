/** Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1] */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  let freqCounter = {};

  for (let i = 0; i < nums.length; i++) {
    let curr = freqCounter[nums[i]] || 0;
    freqCounter[nums[i]] = curr + 1;
  }

  let Ordered = Object.entries(freqCounter).sort((a, b) => b[1] - a[1]);

  let out = [];

  for (let i = 0; i < k; i++) {
    out.push(Ordered[i][0]);
  }
  return out;
};
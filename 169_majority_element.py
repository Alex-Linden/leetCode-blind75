"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''O(n) and o(1) solution'''
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res

#         res = nums[0]
#         freq_most = 1
#         freq = {}

#         for num in nums:
#             freq[num] = freq.get(num, 0) + 1
#             if freq[num] > freq_most:
#                 res = num
#                 freq_most = freq[num]

#         return res
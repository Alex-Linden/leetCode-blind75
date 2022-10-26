"""Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity."""


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            i = (l + r) // 2
            if nums[i] == target:
                return i
            elif nums[i] > target:
                r = i - 1
            elif nums[i] < target:
                l = i + 1

        return -1

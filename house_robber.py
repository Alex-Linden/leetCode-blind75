class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            tmp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = tmp

        return rob2


    def house_robber_2(self, nums):
        return max(nums[0], self.rob(nums[1:0]), self.rob(nums[;-1]))

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        动态规划
        时间复杂度(n2)
        """
        if len(nums) == 0:
            return 0

        # memo[i] [0..i]组成的最长上升子序列的长度(一定以nums[i]结尾)
        memo = [1] * (len(nums))
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    memo[i] = max(memo[i], memo[j] + 1)
        result = 0
        for item in memo:
            result = max(result,item)
        return result

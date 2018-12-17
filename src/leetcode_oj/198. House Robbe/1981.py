class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        偷[0,x]范围内的房子 x取值范围[2,n-1]
        memo(x) = max(nums[i]+memo[i-2],memo[i-1])
        优化
        偷[0,x]范围内的房子 x取值范围[0,n-1]
        memo(x) = max(nums[i]+memo[i],memo[i+1])
        """
        n = len(nums)
        memo = [0] * (n+2)
        memo[0] = nums[0]
        memo[1] = nums[1]
        for i in range(0, n):
            memo[i+2] = max(nums[i] + memo[i], memo[i + 1])
        return memo[-1]

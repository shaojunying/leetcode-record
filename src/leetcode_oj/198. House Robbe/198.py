class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        偷[x,n-1]范围内的房子
        memo(x) = max(nums(x)+memo(x+2),nums(x+1)+memo(x+3)...,
                        nums[n-3]+memo(n-1),nums[n-2](+memo(n)),nums[n-1](+memo(n+1)))
        优化
        memo(x) = max(nums[i]+memo[i+2],memo[i+1])
        """
        n = len(nums)
        memo = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            memo[i] = max(nums[i] + memo[i + 2], memo[i + 1])
        return memo[0]

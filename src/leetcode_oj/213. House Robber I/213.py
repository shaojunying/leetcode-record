class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        return max(self.helper(0,n-2,nums),self.helper(1,n-1,nums))

    # 求[start,end]之间能偷的最大价值
    def helper(self, start, end,nums):
        n = end - start + 1
        memo = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            memo[i] = max(nums[i+start] + memo[i + 2], memo[i + 1])
        return memo[0]

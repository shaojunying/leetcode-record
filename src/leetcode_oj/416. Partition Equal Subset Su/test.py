class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 首先计算nums的和
        sum = 0
        for num in nums:
            sum += num
        if sum % 2 == 1:
            return False
        C = sum / 2

        memo = [0] * (C + 1)
        # 首先将第一行进行初始化
        for j in range(C + 1):
            memo[j] = (nums[0] == j)
        # 之后依次计算每个物品
        for i in range(1, len(nums)):
            # 依次考虑所有背包容量的情况
            for j in range(C, nums[i] - 1, -1):
                memo[j] = memo[j] or memo[j - nums[i]]
        return memo[C]

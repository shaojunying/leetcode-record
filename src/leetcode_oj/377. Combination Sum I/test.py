class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = [0]*(target+1)
        memo[0]=1
        for i in range(target+1):
            for j in range(len(nums)):
                if nums[j]<i:
                    continue
                memo[i] += memo[i-nums[j]]
        return memo[target]


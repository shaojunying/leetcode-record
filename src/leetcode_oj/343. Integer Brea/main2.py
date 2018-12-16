class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        assert n >= 2
        memo = [-1] * (n + 1)

        for i in range(1, n + 1):
            for j in range(1, i):
                memo[i] = max(memo[i], (i - j) * memo[j], (i - j) * j)
        return memo[n]


s = Solution()
print(s.integerBreak(10))

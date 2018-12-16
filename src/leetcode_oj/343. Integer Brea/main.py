class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        assert n >= 2
        memo = [-1]*(n+1)
        return self.helper(n,memo)

    def helper(self, n,memo):
        if n == 1:
            return 1
        if memo[n] != -1:
            return memo[n]
        max_value = -1
        for i in range(1, n):
            max_value = max(max_value, (n - i) * self.helper(i,memo), (n - i) * i)
        memo[n] = max_value
        return max_value


s = Solution()
print(s.integerBreak(10))

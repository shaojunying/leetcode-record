from math import sqrt


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [-1] * (n + 1)
        return self.helper(n, memo)

    def helper(self, n, memo):
        print(n, memo)
        if n == 0:
            return 0
        if memo[n] != -1:
            return memo[n]
        memo[n] = 1 + self.helper(n - 1, memo)
        for i in range(2, int(sqrt(n))+1):
            print(n, i ** 2)
            memo[n] = min(memo[n],1+ self.helper(n - i ** 2, memo))
        return memo[n]


s = Solution()
print(s.numSquares(12))

import sys


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [sys.maxsize] * (n + 1)
        memo[0] = 0
        for i in range(1, n + 1):
            for j in range(1, i+1):
                if j ** 2 > i:
                    break
                memo[i] = min(memo[i], 1 + memo[i - j ** 2])
        print(memo)
        return memo[n]


s = Solution()
print(s.numSquares(7691))

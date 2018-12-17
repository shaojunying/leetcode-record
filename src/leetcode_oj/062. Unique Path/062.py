class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = [[0] * n for _ in range(m)]
        memo[0][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                memo[i][j] = memo[i][j]+memo[i][j - 1]
                memo[i][j] = memo[i][j]+memo[i - 1][j]
        return memo[-1][-1]

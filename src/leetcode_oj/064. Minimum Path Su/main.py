class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        table = [[0] * len(grid[0]) for _ in range(len(grid))]
        table[0][0] = grid[0][0]
        m = len(grid[0])
        n = len(grid)
        for i in range(m):
            table[0][i] = grid[0][i] + table[0][i - 1]
        for i in range(n):
            table[i][0] = grid[i][0] + table[i - 1][0]

        for i in range(1, n):
            for j in range(1, m):
                table[i][j] = min(table[i][j - 1], table[i - 1][j]) + grid[i][j]

        return table[-1][-1]


s = Solution()
print(s.minPathSum([
    [1]
]))

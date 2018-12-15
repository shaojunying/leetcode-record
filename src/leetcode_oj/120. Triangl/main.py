class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return 0
        f = [0]*(len(triangle[-1])+1)
        for line in triangle[::-1]:
            for i in range(len(line)):
                f[i] = line[i]+min(f[i],f[i+1])
        return f[0]



s = Solution()
print(s.minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))

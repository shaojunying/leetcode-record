class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        类似于要考虑体积和重量的01背包问题
        """

        memo = [[0] * (n + 1) for _ in range(m + 1)]
        useless = []

        for str in strs:
            zero_count = str.count('0')
            one_count = str.count('1')

            if (zero_count,one_count) in useless:
                continue

            for j in range(m, zero_count - 1, -1):
                for k in range(n, one_count - 1, -1):
                    memo[j][k] = max(memo[j][k], memo[j - zero_count][k - one_count] + 1)
            useless.append((zero_count,one_count))
        return memo[m][n]

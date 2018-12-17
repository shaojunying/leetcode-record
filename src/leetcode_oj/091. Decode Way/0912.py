class Solution:
    @staticmethod
    def numDecodings(s):
        """
        :type s: str
        :rtype: int
        """
        # memo[i]表示s的后i位组成的字符串数

        s_len = len(s)
        if s_len == 0 or s[0] == "0":
            return 0

        # 考虑输入串只有两个的情况
        memo = [-1] * (len(s) + 1)
        memo[0] = 1
        for i in range(1, s_len + 1):
            memo[i] = memo[i - 1]
            if s[i - 1] == "0":
                memo[i] = 0
            if i > 1 and 10 <= int(s[i - 2:i]) <= 26:
                memo[i] += memo[i - 2]
        return memo[-1]


print(Solution.numDecodings("12"))

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = [-1] * (len(s) + 1)
        memo[0] = 1
        return self.helper(s, len(s), memo)

    def helper(self, s, i, memo):
        if memo[i] != -1:
            return memo[i]
        memo[i] = self.helper(s, i - 1, memo)
        if s[i - 1] == "0":
            memo[i] = 0
        if i > 1 and 10 <= int(s[i - 2:i]) <= 26:
            memo[i] += self.helper(s, i - 2, memo)

        return memo[i]

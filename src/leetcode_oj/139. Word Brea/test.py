class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        memo[i]指s中的[0..i-1]是否都能与wordDict匹配
        """
        memo = [False] * (len(s) + 1)
        memo[0] = True
        # for i in range(len(memo)):
        #     for j in range(0, i):
        #         if memo[j] and s[j:i] in wordDict:
        #             memo[i] = True
        wordDict = set(wordDict)
        for i in range(len(memo)):
            for str in wordDict:
                if not memo[i] and i - len(str) >= 0:
                    memo[i] = memo[i - len(str)] and str == s[i - len(str):i]
        return memo[-1]

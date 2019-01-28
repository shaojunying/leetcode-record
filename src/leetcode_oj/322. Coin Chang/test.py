class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #
        memo = [amount+1] * (amount + 1)
        for coin in coins:
            for i in range(coin, len(memo)):
                memo[i] = min(memo[i], memo[i - coin] + 1)
        if memo[amount] == amount+1:
            return -1
        return memo[amount]

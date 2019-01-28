class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 总天数小于两天时最大收益一定为0
        if len(prices) <= 1:
            return 0
        # 第i天拥有股票的情况下的最大收益
        hold = [0] * 3
        # 第i天不拥有股票的最大收益
        cash = [0] * 3

        hold[0] = -prices[0]
        hold[1] = max(hold[0], -prices[1])
        cash[1] = max(cash[0], -prices[0] + prices[1])

        for i in range(2, len(prices)):
            # 第i天拥有股票的最大收益为 i-1天拥有,i-2天没有股票+i天买入
            hold[i % 3] = max(hold[(i - 1) % 3], cash[(i - 2) % 3] - prices[i])
            # 第i天没有股票的最大收益为 i-1天没有股票,i-1天拥有股票+i天卖出
            cash[i % 3] = max(cash[(i - 1) % 3], hold[(i - 1) % 3] + prices[i])
        return cash[(len(prices) - 1) % 3]

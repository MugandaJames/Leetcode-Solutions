class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = float('inf')
        max_profit = 0

        for price in prices:

            # update minimum buy price
            if price < min_price:
                min_price = price

            # calculate profit if selling now
            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit

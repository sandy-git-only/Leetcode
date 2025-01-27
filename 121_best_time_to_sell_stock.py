class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price = 999
        profit = 0
        for price in prices:
            if price < buy_price:
                buy_price = price
            else:
                profit = max(profit, price - buy_price)
        return profit


solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([7,6,4,3,1]))

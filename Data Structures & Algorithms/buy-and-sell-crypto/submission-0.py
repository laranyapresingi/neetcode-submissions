class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0

        for i in range(1,n):
            for j in range(i,-1,-1):
                if prices[j] < prices[i]:
                    profit=max(profit,prices[i]-prices[j])

        return profit
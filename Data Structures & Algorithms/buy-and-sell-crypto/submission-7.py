class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a,b=0,1
        maxP=0

        while b < len(prices):
            if prices[b] <= prices[a]:
                a=b
                b+=1
            else:
                maxP=max(maxP,prices[b]-prices[a])
                b+=1
        return maxP
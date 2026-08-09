class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = i+1
        profit = 0
        n = len(prices)
        while i<j and i<n-1 and j<n:
            if prices[i] < prices[j]:
                profit = max(profit,prices[j]-prices[i])
                j+=1
            else:
                i+=1
                j=i+1
        return profit
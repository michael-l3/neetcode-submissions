class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        minNum = prices[0]

        for i in range(1,len(prices)): 
            price = prices[i]
            profit = price - minNum 

            maxProfit = max(maxProfit,profit)
            minNum = min(price,minNum)
        
        return maxProfit
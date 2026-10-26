class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #can be neg so tuple time
        #dimensions: index of i, and if i can buy or not 
        memo = {}

        def dfs(i,canBuy): 
            if i >= len(prices): 
                return 0 
            
            if (i,canBuy) in memo: 
                return memo[(i,canBuy)]
            
            profit = 0
            #so we buy here or we can wait, when we buy our profit goes down
            if canBuy: 
                buy = -prices[i] + dfs(i+1,False)
                wait = dfs(i+1,True)
                profit = max(buy,wait)
            else: 
                #we cant buy and we either have to wait to sell or to sell rn 
                #selling now 
                sell = prices[i] + dfs(i+2,True)
                wait = dfs(i+1,False)
                profit = max(sell,wait)
            
            memo[(i,canBuy)] = profit 
            return profit

        
        return dfs(0,True)
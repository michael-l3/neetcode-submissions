class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #cool down of one day 
        #and you can only buy 1 neetcoin 
        #cant sell 
        #we need to cases, one where we buy and one where we dont, and the day we are on 
        memo = {}

        def dfs(day,buying): 
            #cant sell
            if day >= len(prices): 
                return 0 
            #alr cached for largest amount
            if (day,buying) in memo: 
                return memo[(day,buying)]
            
            #now the case if buying
            if buying: 
                #if we are buyijng money is leaving our wallet , the following selling and stuff
                buy = -prices[day] + dfs(1+day,False)
                
                #if we are just waiting to buy a different day 
                waiting = dfs(day+1,True)
                
                memo[(day,buying)] = max(buy,waiting)
            else: 
                #now we are on cooldown and must sell now, and we can buy the day after next day
                sell = prices[day] + dfs(2+day,True)
                #otherwise we are waiting to sell and still have our stock so we cant buy yet
                waiting = dfs(1+day,False)
                memo[(day,buying)] = max(sell,waiting)
            
            return memo[(day,buying)]

            

        
        return dfs(0,True)
        
        
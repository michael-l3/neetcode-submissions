class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(currAmount): 
            if currAmount == 0: 
                return 0 
            
            if currAmount < 0: 
                return float('inf') 
            
            if currAmount in memo: 
                return memo[currAmount]

            #now we have to go through the coins 
            best = float('inf')
            for coin in coins: 
                amount = currAmount - coin 
                currBest = dfs(amount)
                best = min(best,currBest) 
            
            memo[currAmount] = 1 + best
            return memo[currAmount]
        
        result = dfs(amount)
        if result == float('inf'): 
            return  -1 
        
        return result


            
        
        
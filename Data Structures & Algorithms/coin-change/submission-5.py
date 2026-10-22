class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remaining):
            if remaining == 0:  #as in if the remainder == 0 then we dont need any coins anymore
                return 0
            
            if remaining < 0: 
                return float('inf')
            
            if remaining in memo: 
                return memo[remaining]
            
            best = float('inf')
            for coin in coins: 
                currBest = dfs(remaining - coin)
                best = min(best,currBest)
            
            memo[remaining] = 1 + best 
            return memo[remaining]
            
        result = dfs(amount)

        if result != float('inf'): 
            return result 
        else: 
            return -1 

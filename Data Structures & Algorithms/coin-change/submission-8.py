class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remaining): 
            if remaining == 0:  #one way to make the combo
                return 0
            
            if remaining < 0: 
                return float('inf')
            
            if remaining in memo: 
                return memo[remaining]
            
            best = float('inf')
            for coin in coins: 
                if remaining - coin < 0: 
                    continue 
                currBest = 1 + dfs(remaining-coin)
                best = min(currBest,best)
            
            memo[remaining] = best 
            return best
        
        result = dfs(amount)
        if result != float('inf'): 
            return result 
        else: 
            return -1
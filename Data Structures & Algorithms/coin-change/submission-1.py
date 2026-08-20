class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dynamic programming 
        coins.sort()
        memo = {0:0}

        for i in range(1,amount + 1): 
            minCoins = float('inf')

            for coin in coins: 
                if i - coin < 0: 
                    break 
                minCoins = min(minCoins, memo[i - coin] + 1)
            
            memo[i] = minCoins
        
        if memo[amount] != float('inf'): 
            return memo[amount]
        else:
            return -1
            
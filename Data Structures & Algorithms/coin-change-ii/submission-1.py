class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #2d dynamic 
        #keep track of index, currAmoutn 
        #row will be amount, and coins will be column
        memo = [] 
        for r in range(amount+1): #amount plus 1 bc 0 to amount 
            row = [] 
            for c in range(len(coins)): 
                row.append(-1)
            memo.append(row)

        
        #now the dp: 
        def dp(currAmount,i): 
            if i >= len(coins): 
                return 0 
            if currAmount == amount:  #one way to make it
                return 1
            if currAmount > amount: 
                return 0 
            
            #now if it is in our cache 
            if memo[currAmount][i] != -1: 
                return memo[currAmount][i]
            
            #take the number again 
            takeAgain = dp(currAmount + coins[i],i)
            #take the next number 
            takeNext = dp(currAmount, i+1)
            memo[currAmount][i] = takeAgain + takeNext 
        
            return memo[currAmount][i]
        
        return dp(0,0)
        

class Solution:
    def climbStairs(self, n: int) -> int:
        #only doing memoization 
        memo = {}

        #dfs our way to the top 
        def dfs(i): 
            #base case
            if i > n: 
                return 0
            
            if i == n: 
                return 1
            
            #return cached results
            if i in memo: 
                return memo[i]
            
            #either take one or two steps from here
            oneStep = dfs(1+i)
            twoStep = dfs(2+i)

            memo[i] = oneStep + twoStep 
            return memo[i]

        
        return dfs(0)


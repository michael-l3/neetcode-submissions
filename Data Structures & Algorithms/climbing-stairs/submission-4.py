class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(i): 
            if i == n: 
                return 1 
            
            if i >= n: 
                return 0
            
            if i in memo: 
                return memo[i]
            
            oneStep = dfs(i+1)
            twoStep = dfs(i+2)

            memo[i] = oneStep + twoStep 
            return memo[i]
        
        return dfs(0)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dfs(i): 
            if i >= len(cost): 
                return 0
            
            if i in memo: 
                return memo[i]
            
            oneStep = dfs(i+1)
            twoStep = dfs(i+2)

            memo[i] = cost[i] + min(oneStep,twoStep)
            return memo[i]
        
        return min(dfs(0),dfs(1))
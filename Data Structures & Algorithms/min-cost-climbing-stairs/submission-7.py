class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dfs(i): 
            if i >= len(cost): 
                return 0        #doesnt cost anymore we made it to top 
            
            if i in memo: 
                return memo[i]
            
            oneStep = dfs(i+1)
            twoStep = dfs(i+2)

            memo[i] = cost[i] + min(oneStep,twoStep)
            return memo[i]

        
        #we can start at 0 or 1 so 
        return min(dfs(0),dfs(1))
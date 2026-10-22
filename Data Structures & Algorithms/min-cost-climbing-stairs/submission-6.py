class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {} 

        def dfs(i): 
            #so if we are passed the last index that means we made it 
            if i >= len(cost): 
                return 0
            
            if i in memo: 
                return memo[i]
            
            oneStep = cost[i] + dfs(i+1)
            twoStep = cost[i] + dfs(i+2)

            memo[i] = min(oneStep,twoStep)
            return memo[i]
        
        return min(dfs(0),dfs(1)) #min cost starting from either 0 or 1 
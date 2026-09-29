class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #always using memo for dp questions from now on 
        memo = {}
        n = len(cost)

        def dfs(i): 
            if i >= n: 
                return 0 
            
            if i in memo: 
                return memo[i]
            
            oneStep = dfs(i+1)
            twoStep = dfs(i+2)

            memo[i] = cost[i] + min(oneStep,twoStep)
            return memo[i]
        
        return min(dfs(0),dfs(1))

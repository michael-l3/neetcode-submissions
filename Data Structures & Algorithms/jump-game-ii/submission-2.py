class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {} 

        def dfs(i): 
            #we already made it to the end then so 0 steps needed
            if i >= len(nums) - 1: 
                return 0 
            
            if i in memo: 
                return memo[i]
            
            max_jump = min(i+nums[i],len(nums)-1)
            minimum = float('inf')

            for next_jump in range(i+1,max_jump+1): 
                jump = dfs(next_jump)
                
                if jump != float('inf'): 
                    minimum = min(minimum,1 + jump)
            
            memo[i] = minimum
            return memo[i]

        return dfs(0)
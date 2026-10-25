class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i): 
            if i >= len(nums): 
                return 0 
            
            if i in memo: 
                return memo[i]
            
            rob1 = nums[i] + dfs(i+2)
            rob2 = dfs(i+1)

            memo[i] = max(rob1,rob2)
            return memo[i]
        
        #we can start at either 
        return dfs(0)
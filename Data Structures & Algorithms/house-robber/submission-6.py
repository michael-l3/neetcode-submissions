class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {} 

        def dfs(i): 
            if i >= len(nums): 
                return 0 
            
            if i in memo: 
                return memo[i]
            
            rob1 = dfs(i+1)
            rob2 = nums[i] + dfs(i+2)

            memo[i] = max(rob1,rob2)
            return memo[i]
        
        return max(dfs(0),dfs(1))
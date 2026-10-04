class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i): 
            if i >= len(nums): 
                return 0
            
            if i in memo: 
                return memo[i]
            
            rob1 = dfs(i+1)
            rob2 = dfs(i+2)

            memo[i] = max(nums[i] + rob2,rob1)
            return memo[i]
            
        return dfs(0)
        
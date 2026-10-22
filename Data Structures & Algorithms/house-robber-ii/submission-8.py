class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
            
        def rob1(lst):
            memo = {} 

            def dfs(i): 
                if i >= len(lst): 
                    return 0 
                
                if i in memo: 
                    return memo[i]
                
                rob1 = dfs(i+1)
                rob2 = lst[i] + dfs(i+2)

                memo[i] = max(rob1,rob2)
                return memo[i]
            
            return max(dfs(0),dfs(1)) 
        
        return max(rob1(nums[:len(nums)-1]),rob1(nums[1:]))
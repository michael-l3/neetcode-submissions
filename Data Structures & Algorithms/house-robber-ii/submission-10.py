class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]

        def rob2(num):
            memo = {}

            def dfs(i): 
                if i >= len(num): 
                    return 0 
                
                if i in memo: 
                    return memo[i]
                
                rob1 = num[i] + dfs(i+2)
                rob2 = dfs(i+1)

                memo[i] = max(rob1,rob2)
                return memo[i]
            
            #we can start at either 
            return dfs(0)
        
        return max(rob2(nums[:len(nums)-1]),rob2(nums[1:]))
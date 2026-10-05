from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def dfs(i): 
            if i >= len(nums) - 1: 
                return True 

            if i in memo: 
                return memo[i]

            #so now we have to establish how far we can jump 
            max_jump = min(i + nums[i],len(nums)-1)
            #becuase we can jump to positions in between we must check for all of those too 
            for next_i in range(i+1,max_jump+1): 
                if dfs(next_i): 
                    memo[i] = True 
                    return True 
            
            memo[i] = False 
            return False
        
        return dfs(0)
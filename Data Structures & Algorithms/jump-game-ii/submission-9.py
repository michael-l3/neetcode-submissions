class Solution:
    def jump(self, nums: list[int]) -> int:
        memo = {}

        def dfs(i): 
            # Base Case: Already at or past the end means 0 more jumps needed
            if i >= len(nums) - 1: 
                return 0  # Fixed: changed from 1 to 0
            
            if i in memo: 
                return memo[i]
            
            minJump = float('inf')
            
            # Figure out jumping: start at i + 1 so we don't call dfs(i) on ourselves
            for j in range(i + 1, i + nums[i] + 1): 
                currJump = 1 + dfs(j)
                minJump = min(currJump, minJump)
            
            memo[i] = minJump
            return minJump
  
        return dfs(0)
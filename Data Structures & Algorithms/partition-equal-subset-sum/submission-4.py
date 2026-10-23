class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {} 

        if sum(nums) % 2 != 0: 
            return False 
        
        target = sum(nums) / 2 

        def dfs(i,remaining): 
            if remaining == 0: 
                return True 
            
            if remaining < 0: 
                return False 
            
            if i in memo: 
                return memo[i]
            
            for j in range(i+1,len(nums)): 
                number = nums[j]
                new_remaining = remaining - number 
                if dfs(j,new_remaining): 
                    return True 
            
            return False


        return dfs(0,target)
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        level = []

        def dfs(i,currSum): 
            if currSum == target: 
                res.append(level.copy())
                return 

            if currSum > target: 
                return 

            if i >= len(nums): 
                return 
            
            level.append(nums[i])
            dfs(i,currSum + nums[i])
            level.pop() 

            #skip 
            dfs(i+1,currSum)
            
        dfs(0,0)
        
        return res
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [] 
        level = []
        
        def dfs(i): 
            if i >= len(nums): 
                res.append(level.copy())
                return 
            
            #take the number 
            level.append(nums[i])
            dfs(i+1)

            #remove the number 
            level.pop() 

            while i+1 < len(nums) and nums[i+1] == nums[i]: 
                i += 1 
            
            dfs(i+1)

        
        dfs(0)
        return res
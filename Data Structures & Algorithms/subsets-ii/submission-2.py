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
            #take the next 
            dfs(i+1)
            #remove and try next 
            level.pop() 

            while i + 1 < len(nums) and nums[i] == nums[i+1]: 
                i += 1 
            
            #skip the curr number all alone
            dfs(i+1)
        
        dfs(0)
        return res
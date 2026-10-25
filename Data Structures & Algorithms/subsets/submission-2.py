class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        level = [] 
        
        def dfs(i): 
            if i >= len(nums): 
                res.append(level.copy())
                return 
            
            #we take the number and move on to the next 
            level.append(nums[i])
            dfs(i+1)

            #we remove number 
            level.pop() 
            #skip the number
            dfs(i+1)
        
        dfs(0)
        return res
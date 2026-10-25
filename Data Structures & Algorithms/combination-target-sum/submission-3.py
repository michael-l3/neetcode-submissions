class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        level = [] 

        def dfs(i,currSum): 
            if i >= len(nums): 
                return 

            if currSum == target: 
                res.append(level.copy())
                return 
                
            if currSum > target: 
                return  
            
            #take the number 
            level.append(nums[i])
            #take the number again 
            dfs(i,currSum + nums[i])

            #remove number if it doesnt work/explore 
            level.pop() 
            #take the next number 
            dfs(i+1,currSum)
        
        dfs(0,0)
        return res
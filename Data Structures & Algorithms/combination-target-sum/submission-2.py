class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        level = [] 

        def dfs(i, currSum): 
            if i >= len(nums): 
                return 

            if currSum > target: 
                return 
            
            if currSum == target: 
                res.append(level.copy())
                return
            
            #we start and build up, take the number and keep taking the number 
            level.append(nums[i])
            dfs(i,currSum + nums[i])
            level.pop() 

            #now we take the next number 
            dfs(i+1, currSum)

        
        dfs(0,0)
        return res 
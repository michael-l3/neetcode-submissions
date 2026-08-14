class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []  
        level = [] 

        def dfs(i, currSum): 
            #base case 
            if currSum == target: 
                res.append(level.copy())
                return 
            #if currSum is too large 
            if currSum > target: 
                return 
            #out of bounds case
            if i >= len(nums): 
                return 
            
            #choose the number at i 
            level.append(nums[i])
            #choose it again 
            dfs(i,currSum+nums[i])
            level.pop() 
            #choose the next number with the previous currSum 
            dfs(i+1,currSum)
        
        dfs(0,0)
        return res
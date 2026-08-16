class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        level = [] 

        def dfs(index, currSum): 
            if currSum == target: 
                res.append(level.copy())
                return 
            
            if currSum > target: 
                return 
            
            if index >= len(nums): 
                return

            #choose the number 
            level.append(nums[index])
            #choose number again 
            dfs(index,currSum + nums[index])
            #no longer need the number too larger or out of bounds 
            level.pop() 
            #next  number 
            dfs(index + 1, currSum)

        dfs(0,0)
        return res
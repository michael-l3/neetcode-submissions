class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        level = [] 

        #chosen unlimted time 
        def dfs(i,currSum): 
            if i >= len(nums): 
                return 

            if currSum > target: 
                return 
            
            if currSum == target: 
                res.append(level.copy())
                return
            #take the curr number until we cant anymore 
            level.append(nums[i])
            dfs(i,currSum + nums[i])
            #it will eventually hit a base case then we got to try a new number or take off
            #number bc the value got too big 
            level.pop() 
            dfs(i+1,currSum)

        
        dfs(0,0)
        return res
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #backtracking 
        res = [] 
        level = [] 

        def dfs(i, currSum): 
            #base Case is where the currSum = target then we append a copy of the level into res 
            if currSum == target: 
                res.append(level.copy()) 
                return 
            
            #now if the currSum is too big then we have to return and try something else 
            if currSum > target: 
                return 
            
            #now if index is out of bounds we go too far out return 
            if i >= len(nums): 
                return 
            
            #now we want to take the first value 
            level.append(nums[i])
            #take it again, until we cant 
            dfs(i,currSum + nums[i])
            #until we cant no more then we try with the next number
            level.pop() 
            dfs(i+1, currSum)
        
        dfs(0,0)
        return res



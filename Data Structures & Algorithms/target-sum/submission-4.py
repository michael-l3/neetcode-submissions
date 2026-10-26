class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #dimension would be index and currSUm 
        #bc it can be negative we are going to use tuple 
        memo = {}

        def dfs(i,currSum): 
            if i > len(nums): 
                return 0 
            if i == len(nums): 
                if currSum == target: 
                    return 1
                else: 
                    return 0
            
            if (i,currSum) in memo: 
                return memo[(i,currSum)]

            #make neg or positive 
            neg = dfs(i+1, currSum - nums[i])
            pos = dfs(i+1, currSum + nums[i])
 
            memo[(i,currSum)] = neg + pos 
            return memo[(i,currSum)]

        
        return dfs(0,0)
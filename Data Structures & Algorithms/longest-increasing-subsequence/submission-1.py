class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i): 
            if i >= len(nums): 
                return 0

            if i in memo: 
                return memo[i]

            best = 1
            for j in range(i+1,len(nums)): 
                if nums[j] > nums[i]: 
                    currBest = dfs(j)
                    best = max(best,1 + currBest)
                
            memo[i] = best 
            return memo[i]
        
        result = 0 

        for i in range(len(nums)): 
            result = max(result,dfs(i))
            
        return result
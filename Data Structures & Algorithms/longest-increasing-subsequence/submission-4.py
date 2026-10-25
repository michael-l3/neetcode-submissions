class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        
        def dfs(i): 
            if i >= len(nums): 
                return 0
            
            if i in memo: 
                return memo[i]
            
            res = 1
            for j in range(i,len(nums)): 
                if nums[j] > nums[i]: 
                    currRes = 1 + dfs(j)
                    res = max(currRes,res)
            
            memo[i] = res 
            return memo[i]
            
        
        res = 0 
        for i in range(len(nums)): 
            curr = dfs(i)
            res = max(res,curr)
        
        return res
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {} 

        def dfs(i): 
            if i >= len(nums): 
                return 0 

            if i in memo: 
                return memo[i]

            curr = 1
            for j in range(i+1,len(nums)): 
                if nums[j] > nums[i]: 
                    currBest = dfs(j)
                    curr = max(curr,1 + currBest)
            
            memo[i] = curr 
            return curr
        
        longest = 0
        for i in range(len(nums)): 
            curr = dfs(i)
            longest = max(longest,curr)
        
        return longest
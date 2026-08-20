class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest = 1
        dp = [1] * len(nums)
        #we need to check the prev longest and if the number is > that 
        
        for i in range(len(nums)): 
            for j in range(i): 

                if nums[j] < nums[i]: 
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)




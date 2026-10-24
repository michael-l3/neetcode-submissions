class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        memo = {}
        
        def dp(currAmount, i):
            # 1. Base Case: Used up all numbers
            if i == len(nums):
                return 1 if currAmount == target else 0
            
            # 2. Dictionary cache lookup (handles negative numbers effortlessly!)
            if (currAmount, i) in memo:
                return memo[(currAmount, i)]
            
            # 3. Choices
            add = dp(currAmount + nums[i], i + 1)
            sub = dp(currAmount - nums[i], i + 1)
            
            # 4. Store and return
            memo[(currAmount, i)] = add + sub
            return memo[(currAmount, i)]
        
        return dp(0, 0)
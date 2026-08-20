class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        result = nums[0]

        for n in nums[1:]: 
            curr = max(n + curr, n)
            result = max(curr, result)
        
        return result
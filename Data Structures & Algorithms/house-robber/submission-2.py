class Solution:
    def rob(self, nums: List[int]) -> int:
        #cant rob two adjacent houses
        maxProfit = 0 

        if len(nums) == 1: 
            return nums[0]
        if len(nums) == 2: 
            return max(nums[0],nums[1])
        
        first = nums[0]
        second = max(nums[0],nums[1])

        for i in range(2,len(nums)): 
            curr = max(first + nums[i], second)
            first = second 
            second = curr 

            maxProfit = max(first, second)
        
        return maxProfit
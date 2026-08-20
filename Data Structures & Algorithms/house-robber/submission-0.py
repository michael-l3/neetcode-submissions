class Solution:
    def rob(self, nums: List[int]) -> int:
        maxProfit = 0 
        n = len(nums)

        if n == 1: 
            return nums[0]
        if n == 2 : 
            return max(nums[0], nums[1])
        
        first = nums[0]
        second = max(nums[0], nums[1])

        for i in range(2,n): 
            curr = max(first + nums[i],second)
            first = second 
            second = curr 
        
        return curr

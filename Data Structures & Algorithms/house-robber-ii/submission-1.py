class Solution:
    def rob(self, nums: List[int]) -> int:
        #just two house rob on two different list one starts at +1 
        maxRob2 = 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2: 
            return max(nums[0],nums[1])

        def rob1(nums):
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
        
        first = rob1(nums[:len(nums) - 1])
        second = rob1(nums[1:])

        return max(first,second)
        

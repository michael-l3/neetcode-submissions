from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n - 1 

        #we are starting from then end and moving the target down to see if we can get to 0
        for i in range(n-1,-1,-1): 
            max_jump = nums[i]

            #now if we can jump from where we are to our target then the new target is our index 
            if i + max_jump >= target: 
                target = i 
            
        #eventually we will make it to 0 if we can hit our target 
        return target == 0
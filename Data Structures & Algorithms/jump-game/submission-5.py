class Solution:
    def canJump(self, nums: list[int]) -> bool:
        furthest = 0 #this is the furhtest index we can get to rn 

        for i in range(len(nums)): 
            jump = nums[i]

            if i > furthest: 
                return False  #that means we are on a stone that we cant even get to 
            
            #if that isnt the case we need to keep updating furthest 
            furthest = max(furthest, i + jump)

            if furthest >= len(nums) -1 : 
                return True 
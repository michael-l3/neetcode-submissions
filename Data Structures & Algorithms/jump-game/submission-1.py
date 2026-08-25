class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #greedy problem 
        #we are setting the goal equal to the end  
        #then tryign to see if we can make it all the way down using greedy 

        n = len(nums) 
        target = n - 1 

        for i in range(n - 1, -1, -1): 
            maxJump = nums[i] 

            if i + maxJump >= target: 
                target = i  
        
        return target == 0
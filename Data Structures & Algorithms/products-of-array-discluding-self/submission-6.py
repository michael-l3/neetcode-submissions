class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) 

        prefix = 1 #"left" of the number
        for i in range(len(nums)): 
            res[i] = prefix 
            prefix *= nums[i] 
        
        postfix = 1 #"right" of said number and multiple it 
        for i in range(len(nums) -1,-1,-1): 
            res[i] *= postfix 
            postfix *= nums[i] 
        
        return res

 

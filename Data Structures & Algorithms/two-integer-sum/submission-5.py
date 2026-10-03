class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
    
        for i in range(len(nums)): 
            number = nums[i]
            complement = target - number 

            if complement in m: 
                return[m[complement],i]
            
            m[number] = i 
        
        return -1
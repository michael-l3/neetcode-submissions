class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = []

        for i in range(len(nums)): 
            number = nums[i]

            if i > 0 and nums[i] == nums[i-1]: 
                continue
 
            l = i + 1
            r = len(nums) - 1 

            while l < r: 
                threeSum = number + nums[l] + nums[r]

                if threeSum < 0: 
                    l += 1 
                elif threeSum > 0: 
                    r -= 1 
                else: 
                    res.append([number,nums[l],nums[r]])
                    l += 1 
                    r -= 1
                    
                    while l < r and nums[l] == nums[l-1]: 
                        l += 1 
                        
        return res
                
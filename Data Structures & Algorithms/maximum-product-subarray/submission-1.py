class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = 1
        currMin = 1
        res = max(nums)

        for number in nums: 
            new1 = currMax * number 
            new2 = currMin * number 

            currMax = max(new1,new2,number)
            currMin = min(new1,new2,number)

            res = max(new1,new2,res)
        
        return res
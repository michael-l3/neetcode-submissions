class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        #keep track of maxSub
        #and lowest in case there are two negatives 
        curr_min = 1 
        curr_max = 1 

        for n in nums: 
            if n == 0: 
                curr_min = 1 
                curr_max = 1 
                continue 
            
            tmp = curr_max * n 
            curr_max = max(curr_max * n, curr_min * n, n)
            curr_min = min(curr_min *n, tmp, n)

            res = max(res,curr_max)
        
        return res
            



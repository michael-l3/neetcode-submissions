class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = max(nums)
        curr_largest = 1
        curr_smallest = 1 

        for n in nums: 
            temp = curr_largest * n
            curr_largest = max(temp, curr_smallest * n, n)
            curr_smallest = min(temp, curr_smallest * n, n)

            if curr_largest > maxProduct: 
                maxProduct = curr_largest 
        
        return maxProduct
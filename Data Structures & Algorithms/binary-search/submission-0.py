class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1 

        while l <= r: 
            mid = (r + l) // 2 

            if nums[mid] < target: 
                l += 1 
            elif nums[mid] > target: 
                r -= 1
            else: 
                return mid 
        
        return -1
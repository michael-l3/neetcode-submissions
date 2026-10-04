class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSub = 0 
        uniqueSet = set(nums) 

        for n in nums: 
            if n - 1 not in uniqueSet: 
                length = 1 
            
                while n + length in uniqueSet: 
                    length += 1 
                longestSub = max(length, longestSub) 
        
        return longestSub


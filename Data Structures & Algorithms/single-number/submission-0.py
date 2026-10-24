class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}

        for number in nums: 
            if number in d: 
                d[number] += 1 
            else: 
                d[number] = 1 
        
        for number,value in d.items(): 
            if value == 1: 
                return number
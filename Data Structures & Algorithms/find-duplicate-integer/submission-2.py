class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()

        for number in nums: 
            if number in s: 
                return number            
            s.add(number)
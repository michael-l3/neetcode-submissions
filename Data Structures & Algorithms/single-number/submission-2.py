class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #rules here for bit minip 
        #a XOR 0 is just a 
        # number XOR number = 0 

        a = 0 
        for number in nums: 
            a ^= number 
        
        return a
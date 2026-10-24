class Solution:
    def hammingWeight(self, n: int) -> int:
        #trick is to & with number 1 less than current number until the number is 0 

        ans = 0 

        while n != 0: 
            ans += 1 
            n = n & (n-1)
        
        return ans
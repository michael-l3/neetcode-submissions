class Solution:
    def countSubstrings(self, s: str) -> int:
        longest = 0
        n = len(s)

        for i in range(n): 
            #odd case 
            l = i 
            r = i 

            while l >= 0 and r <= n - 1 and s[l] == s[r]: 
                longest += 1
                l -= 1 
                r += 1 
            
            #even case 
            l = i
            r = i + 1 

            while l >= 0 and r <= n - 1 and s[l] == s[r]: 
                longest += 1
                l -= 1 
                r += 1 
            
        return longest


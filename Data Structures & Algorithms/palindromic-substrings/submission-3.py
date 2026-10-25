class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        #start in the middle, then expand 
        for i in range(len(s)): 
            #odd case
            l = i
            r = i 

            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]: 
                res += 1
                l -= 1 
                r += 1

            #even case
            l = i
            r = i + 1

            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]: 
                res += 1
                l -= 1 
                r += 1 
        
        return res
            

            
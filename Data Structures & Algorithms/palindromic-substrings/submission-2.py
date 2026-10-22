class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0 

        for i in range(len(s)): 
            #odd case 
            l = i 
            r = i 

            while l <= r and l >=0 and r <= len(s) - 1: 
                if s[l] == s[r]: 
                    count += 1
                elif s[l] != s[r]: 
                    break 
                
                l -= 1 
                r += 1 
            
            #even case 
            l = i 
            r = i + 1

            while l <= r and l >=0 and r <= len(s) - 1: 
                if s[l] == s[r]: 
                    count += 1
                elif s[l] != s[r]: 
                    break 
                
                l -= 1 
                r += 1 
        
        return count
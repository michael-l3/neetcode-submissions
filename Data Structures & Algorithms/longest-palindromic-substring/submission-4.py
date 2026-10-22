class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxLength = 0
        #will need to create an even and an odd case  
        #go from the character and go out 
        
        for i in range(len(s)): 
            #for our odd case 
            l = i 
            r = i 

            while l <= r and l >=0 and r <= len(s) -1: 
                if s[l] == s[r] and len(s[l:r+1]) > maxLength: 
                    maxLength = len(s[l:r+1])
                    res = s[l:r+1]
                elif s[l] != s[r]: 
                    break
                l -= 1 
                r += 1 
            
            #for our even case 
            l = i 
            r = i + 1

            while l <= r and l >=0 and r <= len(s) -1: 
                if s[l] == s[r] and len(s[l:r+1]) > maxLength: 
                    maxLength = len(s[l:r+1])
                    res = s[l:r+1] 
                elif s[l] != s[r]:
                    break

                l -= 1 
                r += 1  
        
        return res
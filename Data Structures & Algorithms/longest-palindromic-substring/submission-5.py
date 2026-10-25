class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        longest = 0 
        
        #start in the middle, then expand 
        for i in range(len(s)): 
            #odd case
            l = i
            r = i 

            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]: 
                currLength = r - l + 1 
                if currLength > longest: 
                    res = s[l:r+1]
                    longest = currLength 
                l -= 1 
                r += 1

            #even case
            l = i
            r = i + 1

            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]: 
                currLength = r - l + 1 
                if currLength > longest: 
                    res = s[l:r+1]
                    longest = currLength  
                
                l -= 1 
                r += 1 
        
        return res
            

            
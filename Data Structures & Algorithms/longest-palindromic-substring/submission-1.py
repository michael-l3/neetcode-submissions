class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        longest = 0 
        n = len(s)
        #there will be an odd case and an even case 
        #so in an odd case l,r = 0 
        # in even l = 0 r = 1 

        for i in range(n): 
            l,r =i,i 

            while l >= 0 and r <= n -1 and s[l] == s[r]: 
                currLength = (r - l) + 1 
                if currLength > longest: 
                    longest = currLength 
                    res = s[l:r+1]
                l -= 1 
                r += 1 
            
            l,r = i,i+1

            while l >= 0 and r <= n -1 and s[l] == s[r]: 
                currLength = (r - l) + 1 
                if currLength > longest: 
                    longest = currLength 
                    res = s[l:r+1]
                l -= 1 
                r += 1 
        
        return res
             
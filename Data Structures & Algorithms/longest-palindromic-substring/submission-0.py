class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = "" 
        longest = 0
        n = len(s)

        for i in range(n): 
            #odd case 
            l = i 
            r = i 

            while l >= 0 and r <= n - 1 and s[l] == s[r]: 
                curr = (r - l) + 1

                if curr > longest: 
                    longest = curr 
                    res = s[l:r+1]
                l -= 1 
                r += 1 
            
            #even case 
            l = i
            r = i + 1 

            while l >= 0 and r <= n - 1 and s[l] == s[r]: 
                curr = (r - l) + 1

                if curr > longest: 
                    longest = curr 
                    res = s[l:r+1]
                l -= 1 
                r += 1 
            
        return res


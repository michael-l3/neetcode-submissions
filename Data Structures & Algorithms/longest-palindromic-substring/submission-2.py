class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        currentMax = 0

        for i in range(len(s)): 

            l = i 
            r = i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr = r - l + 1 
                if curr > currentMax:
                    currentMax = curr
                    res = s[l : r + 1]
                
                l -= 1 
                r += 1 

            # 2. Even length case (center between i and i + 1)
            l = i 
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr = r - l + 1 
                if curr > currentMax:
                    currentMax = curr
                    res = s[l : r + 1] 
                
                l -= 1 
                r += 1 
        
        return res
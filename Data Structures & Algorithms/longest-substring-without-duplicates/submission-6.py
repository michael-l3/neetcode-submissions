class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 
        window = {}
        l = 0 

        for r in range(len(s)): 
            ch = s[r]

            #if it is in the window then we know there is a dupe
            if ch in window: 
                l = max(l,window[ch]+1)
            
            window[ch] = r 
            currWindow = r - l + 1 
            longest = max(longest,currWindow)
        
        return longest

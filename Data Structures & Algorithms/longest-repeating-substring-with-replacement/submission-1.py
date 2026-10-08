class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0 
        window = {} 
        l = 0 

        for r in range(len(s)): 
            ch = s[r]

            #add it to our window
            if ch in window: 
                window[ch] += 1 
            else: 
                window[ch] = 1  
            
            #see the most freq value 
            freq = max(window.values())

            #we need to strink
            while (r - l - freq) >= k: 
                window[s[l]] -= 1 
                l += 1 
            
            currLength = r - l + 1 
            longest = max(longest,currLength)
        
        return longest


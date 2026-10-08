class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {} 
        window = {}

        for ch in t: 
            if ch in tCount: 
                tCount[ch] += 1
            else: 
                tCount[ch] = 1 
        
        need = len(tCount)
        have = 0 
        res = [-1,-1]
        l = 0 
        currMin = float('inf')

        for r in range(len(s)): 
            ch = s[r]

            if ch in window: 
                window[ch] += 1 
            else: 
                window[ch] = 1 
        
            if ch in tCount and window[ch] == tCount[ch]: 
                have += 1 
            
            while have == need: 
                currLength = r - l + 1 
                if currLength < currMin: 
                    res = [l,r]
                    currMin = currLength 
                
                #now we need to strink it 
                leftChar = s[l]
                window[leftChar] -= 1 

                if leftChar in tCount and window[leftChar] < tCount[leftChar]: 
                    have -= 1 
                
                l += 1 
        l,r = res
        if currMin == float('inf'): 
            return "" 
        
        return s[l:r+1]




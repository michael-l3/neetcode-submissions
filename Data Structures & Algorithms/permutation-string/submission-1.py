class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #I think it has to have exactly that many characters 
        s1M = {}
        window = {}
        
        for ch in s1: 
            if ch in s1M: 
                s1M[ch] += 1 
            else:
                s1M[ch] = 1 
        
        l = 0 
        need = len(s1M)
        have = 0

        for r in range(len(s2)): 
            ch = s2[r]

            if ch not in s1M: 
                window = {}
                have = 0
                l = r + 1
                continue

            if ch in window: 
                window[ch] += 1 
            else: 
                window[ch] = 1 
            
            if window[ch] == s1M[ch]:
                have += 1 
            
            while window[ch] > s1M[ch]: 
                leftChar = s2[l]
                window[leftChar] -= 1 

                if window[leftChar] < s1M[leftChar]: 
                    have -= 1
                
                l += 1
            
            if need == have: 
                return True 

        return False

            
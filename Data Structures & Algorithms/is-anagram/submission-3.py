class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        tCount = {}

        for ch in s: 
            if ch not in sCount: 
                sCount[ch] = 1
            else: 
                sCount[ch] += 1 

        for ch in t: 
            if ch not in tCount: 
                tCount[ch] = 1
            else: 
                tCount[ch] += 1 
        
        if sCount != tCount: 
            return False 
        
        return True
         
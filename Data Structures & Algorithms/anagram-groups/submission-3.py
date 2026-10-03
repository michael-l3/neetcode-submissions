class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} 

        for word in strs: 
            a = [0] * 26 

            for ch in word: 
                a[ord(ch)-ord('a')] += 1 
            
            key = tuple(a)

            if key not in res: 
                res[key] = [] 
            
            res[key].append(word)
        
        return list(res.values())
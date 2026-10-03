class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs: 
            res += str(len(word)) + '#' + word 
        
        return res 
        #[Hello,World]
        #5#Hello5#World
    def decode(self, s: str) -> List[str]:
        l = 0 
        res = []
        while l < len(s): 
            r = l 

            while s[r] != '#': 
                r += 1 
            
            lenOfWord = int(s[l:r]) 
            res.append(s[r+1:r+1+lenOfWord])
            l = r + 1 + lenOfWord 
        
        return res

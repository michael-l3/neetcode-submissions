class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digits_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i,currWord): 
            if len(currWord) == len(digits): 
                res.append(currWord)
                return 
            
            for c in digits_to_char[digits[i]]: 
                dfs(i+1,currWord + c)
        
        if digits: 
            dfs(0, "")
        
        return res
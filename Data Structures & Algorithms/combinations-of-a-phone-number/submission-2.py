class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
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

        level = [] 

        def dfs(i): 
            if i >= len(digits): 
                res.append(''.join(level))
                return 
            
            for letter in digits_to_char[digits[i]]: 
                #take the letter
                level.append(letter)
                dfs(i+1)
                #backtrack
                level.pop()

        dfs(0)
        return res


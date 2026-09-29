class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i == len(s): 
                return 1

            if s[i] == "0": 
                return 0 
            
            if i in memo: 
                return memo[i]
            
            #now we can process as a single digit number and just have to worry about the rest of the indexes 
            res = dfs(i+1)

            #now we check if it is a two digit number or a two digit number can be applied 
            if i + 1 < len(s): 
                #we know we can take two digits 
                twoDigit = int(s[i:i+2])
                if 10 <= twoDigit <= 26: 
                    res += dfs(i+2)
            
            memo[i] = res
            return memo[i]
        
        #starts at the index of the string
        return dfs(0)
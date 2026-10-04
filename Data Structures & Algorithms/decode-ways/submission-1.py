class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i): 
            if i == len(s): 
                return 1 

            if s[i] == '0': 
                return 0 

            if i in memo: 
                return memo[i]

            res = dfs(i+1) 

            #check for the two digit numbers 
            if i + 1 < len(s): 
                twoDigit = int(s[i:i+2])
                if 10 <= twoDigit <= 26: 
                    res += dfs(i+2)

            memo[i] = res 
            return memo[i]
        
        return dfs(0)
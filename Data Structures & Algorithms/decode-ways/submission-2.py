class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i): #where i index of where we are
            #so if i hits the end of the string then we know we have one way
            if i == len(s): 
                return 1 
            
            if s[i] == '0': #this cant be the start of anything 
                return 0 
            
            if i in memo: 
                return memo[i]
            
            #check all the single digit numbers 
            res = dfs(i+1)

            #check for two digits
            if i + 1 < len(s): 
                twoDigit = int(s[i:i+2]) 
                if 10 <= twoDigit <= 26: 
                    res += dfs(i+2)
            
            memo[i] = res 
            return res
            
        
        return dfs(0)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #so we have to build out the cache itself 
        #comparing the values and if they equal then we exhausted a letter on both 
        m = len(text1) # this represents everything related to text1 values ie "CAT"
        n = len(text2) # this represents everythign releated to text2 values ie "CRABT"
        memo = [] 

        for r in range(m): 
            row = [] 
            for c in range(n): 
                row.append(-1)
            memo.append(row)
        
        #now we have the cache 
        def dp(r,c): 
            #so our base case if we are out of bounds then return 0 
            if r >= m or c >= n: 
                return 0 
            
            #now if something is already in memo, then we return it 
            if memo[r][c] != -1: 
                return memo[r][c]
            
            #now if the charcters equal each other, so if text1 value == text2 value then we go on and check both sides 
            #of dp, so we exhausted a letter from both so we have to move down now for both
            if text1[r] == text2[c]: 
                memo[r][c] = 1 + dp(r+1,c+1)
            else: 
                #they dont match and we must explore more and take the max of the largest 
                skipText1 = dp(r+1,c)
                skipText2 = dp(r,c+1)
                memo[r][c] = max(skipText1,skipText2)
            
            return memo[r][c]
        
        return dp(0,0)


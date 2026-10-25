class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = len(text1)
        col = len(text2)

        memo = [] 

        for i in range(row): 
            r = [] 
            for j in range(col): 
                r.append(-1)
            memo.append(r)

        def dfs(i,j): 
            #out of bounds 
            if i >= row or j >= col: 
                return 0 

            if memo[i][j] != -1: 
                return memo[i][j]

            res = 0
            #so now we have to see if we match or not 
            #case when match: 
            if text1[i] == text2[j]: 
                res = 1 + dfs(i+1,j+1)
                #we move both of them over 
            else: 
                #then dont match and we have to try both cases where we move the character over 
                #take the max of the one sliding over for both cases
                res = max(dfs(i+1,j),dfs(i,j+1))
            
            memo[i][j] = res 
            return res

        return dfs(0,0)
        
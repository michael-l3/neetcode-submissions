class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])

        memo = [] 

        for i in range(row): 
            r = []
            for j in range(col): 
                r.append(-1)
            memo.append(r)
        
        def dfs(i,j): 
            if memo[i][j] != -1: 
                return memo[i][j]
            
            longest = 1 

            for i_off,j_off in [(0,1),(0,-1),(1,0),(-1,0)]: 
                r = i + i_off
                c = j + j_off 

                if 0 <= r < row and 0 <= c < col and matrix[r][c] > matrix[i][j]: 
                    currLong = 1 + dfs(r,c)
                    longest = max(longest,currLong)
            
            memo[i][j] = longest 
            return longest
        
        res = 0 
        for i in range(row): 
            for j in range(col): 
                res = max(res,dfs(i,j))

        return res
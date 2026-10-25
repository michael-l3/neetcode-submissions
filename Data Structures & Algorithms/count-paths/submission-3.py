class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #all positive so we can use a board
        #figure out our dimensions, I think it is col index and row index
        memo = []

        for i in range(m): 
            row = [] 
            for j in range(n): 
                row.append(-1)
            memo.append(row)
        
        def dfs(r,c): 
            #base case is if we out of bounds 
            if r >= m or c >= n: 
                return 0 
            
            #now we have hit the target one way made it 
            if r == (m-1) and c == (n-1): 
                return 1 
            
            if memo[r][c] != -1: 
                return memo[r][c]
            res = 0

            #i can only go down or right 
            res += dfs(r,c+1)
            res += dfs(r+1,c)

            memo[r][c] = res 
            return res
        
        return dfs(0,0)

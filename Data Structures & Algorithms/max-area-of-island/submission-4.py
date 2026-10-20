class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) 

        def dfs(i,j): 
            #same approach 
            grid[i][j] = 0 

            currentArea = 1
            #check around 
            for i_off,j_off in [(1,0),(-1,0),(0,1),(0,-1)]: 
                r = i + i_off
                c = j + j_off 

                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                    #1 + to account for iteself 
                    currentArea += dfs(r,c)       

            return currentArea     
             
        
        maxArea = 0 
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == 1: 
                    currentArea = dfs(i,j)
                    maxArea = max(maxArea,currentArea)
        
        return maxArea
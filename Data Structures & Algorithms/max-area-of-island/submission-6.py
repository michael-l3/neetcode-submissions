class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #just finding the value of the largest island 
        row = len(grid) 
        col = len(grid[0]) 

        def dfs(i,j): 
            #dont want to use the spot anymore 
            grid[i][j] = 0

            islandSize = 1
            #check around for neighboring connected land 
            for i_off,j_off in [(1,0),(-1,0),(0,1),(0,-1)]: 
                r = i + i_off 
                c = j + j_off

                #check if in bounds 
                if 0 <= r < row and 0 <= c < col and grid[r][c] == 1: 
                    islandSize += dfs(r,c)   

            return islandSize
        
        maxArea = 0 
        for i in range(row): 
            for j in range(col): 
                if grid[i][j] == 1: 
                    currArea = dfs(i,j)
                    maxArea = max(maxArea,currArea)
        
        return maxArea
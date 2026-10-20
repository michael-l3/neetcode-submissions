class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(pos): 
            i,j = pos 
            #we can do check later for the other dfs 
            #now we change all of the '1's into 0 
            grid[i][j] = '0'

            #check around 
            for i_off,j_off in [(1,0),(-1,0),(0,1),(0,-1)]: 
                r = i + i_off
                c = j + j_off 

                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1': 
                    dfs((r,c))
            
        num_island = 0
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == '1': 
                    num_island += 1 
                    dfs((i,j))
        
        return num_island
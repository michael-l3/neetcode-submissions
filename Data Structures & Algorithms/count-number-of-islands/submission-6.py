class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def dfs(i,j): 
            #we dont want to revisit it 
            grid[i][j] = '0' 

            #check around for neighboring connected land 
            for i_off,j_off in [(1,0),(-1,0),(0,1),(0,-1)]: 
                r = i + i_off 
                c = j + j_off

                #check if in bounds 
                if 0 <= r < row and 0 <= c < col and grid[r][c] == '1': 
                    dfs(r,c)        

        num_island = 0
        for i in range(row): 
            for j in range(col): 
                if grid[i][j] == '1': 
                    num_island += 1 
                    dfs(i,j)
        
        return num_island

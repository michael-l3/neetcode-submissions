class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_island = 0 
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j): 
            # change it instantly so we dont revisit 
            grid[i][j] = "0"

            for i_off, j_off in [(0,1),(0,-1),(1,0),(-1,0)]: 
                r = i + i_off 
                c = j + j_off 

                if 0 <= r < m and 0 <= c < n and grid[r][c] == "1": 
                    dfs(r,c)


        #we have to go through the graph
        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == "1": 
                    num_island += 1 
                    dfs(i,j) 

        return num_island 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_island = 0 
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j): 
            #then we check around and if it is bounds and if it is a 0 or 1 --> this is how we know to go back
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0": 
                return 
            
            #now we change this position to 0 so we dont check again 
            grid[i][j] = "0"

            #now check around 
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        #we have to go through the graph
        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == "1": 
                    num_island += 1 
                    dfs(i,j) 

        return num_island 
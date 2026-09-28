from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0 
        m = len(grid)
        n = len(grid[0])

        def dfs(pos):
            i, j = pos 

            # 1. Boundary check MUST come before grid lookup to prevent IndexError
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1: 
                return 0

            # 2. Mark as visited permanently (NO backtracking undo!)
            grid[i][j] = 0

            # 3. Calculate area for this island
            island_size = 1
            for i_off, j_off in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
                r = i + i_off
                c = j + j_off
                island_size += dfs((r, c))
            
            return island_size

        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 1: 
                    current_island = dfs((i, j))
                    maxArea = max(maxArea, current_island)
        
        return maxArea
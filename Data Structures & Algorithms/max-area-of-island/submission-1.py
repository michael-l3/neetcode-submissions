from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0 
        m = len(grid)
        n = len(grid[0])

        def dfs(pos, currArea):
            nonlocal maxArea
            i, j = pos 

            # 1. Boundary check MUST come before grid lookup to prevent IndexError
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1: 
                return currArea

            currArea += 1
            maxArea = max(currArea, maxArea)

            # 2. Mark visited permanently (NO backtracking undo in graph traversal)
            grid[i][j] = 'x'

            # 3. Check other spots, passing the updated currArea and collecting the total back
            for i_off, j_off in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
                r = i + i_off
                c = j + j_off
                currArea = dfs((r, c), currArea)
            
            return currArea

        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 1: 
                    dfs((i, j), 0)
        
        return maxArea
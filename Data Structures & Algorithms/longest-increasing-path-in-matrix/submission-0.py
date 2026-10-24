class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m = len(matrix) 
        n = len(matrix[0])
        
        # Explicitly building your 2D memo board
        memo = []
        for r in range(m): 
            row = []
            for c in range(n): 
                row.append(-1)
            memo.append(row) 
        
        def dfs(row, col):
            # Memo check
            if memo[row][col] != -1: 
                return memo[row][col]

            # Every cell has at least a path length of 1 (itself)
            longest = 1 

            # Check all 4 directions
            for r_off, c_off in [(0, 1), (0, -1), (1, 0), (-1, 0)]: 
                i = row + r_off
                j = col + c_off

                # If the neighbor is within bounds and strictly greater in value
                if 0 <= i < m and 0 <= j < n and matrix[i][j] > matrix[row][col]: 
                    curr_longest = 1 + dfs(i, j)
                    longest = max(curr_longest, longest)
            
            # Save and return the max path found from this cell
            memo[row][col] = longest 
            return longest
        
        # Scan every cell in the matrix because the longest path can start anywhere
        global_max = 0
        for r in range(m):
            for c in range(n):
                global_max = max(global_max, dfs(r, c))
                
        return global_max
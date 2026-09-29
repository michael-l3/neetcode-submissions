from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh_count = 0

        # 1. Count fresh oranges AND enqueue all initial rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        minutes = 0

        while q and fresh_count > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc

                    # Only infect fresh oranges
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Mark as rotten (acts as visited!)
                        fresh_count -= 1  # Decrement fresh count
                        q.append((nr, nc))

            minutes += 1

        return minutes if fresh_count == 0 else -1
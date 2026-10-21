
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()

        # Add every treasure chest to the queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))

        time = 0

        while q:
            # Process every room at the current distance
            for _ in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = time

                # Check all four directions
                for i_off, j_off in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    r = i + i_off
                    c = j + j_off

                    if (0 <= r < rows and
                        0 <= c < cols and
                        grid[r][c] != -1 and
                        (r, c) not in visited):

                        visited.add((r, c))
                        q.append((r, c))

            # Move to the next distance level
            time += 1

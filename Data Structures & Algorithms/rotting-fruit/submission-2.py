from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque() 
        visted = set()
        fresh = 0
        #we have to bfs, so we put all of the rotten ones in the q \
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == 2: 
                    q.append((i,j))
                    visted.add((i,j))
                elif grid[i][j] == 1: 
                    fresh += 1
        
        #so the plan is to go through the entire q, each iteration we decrement if we encounter 1
        #at the end if fresh = 0 return the time, if not then return -1 (not possible)
        time = 0 
        while q and fresh > 0: 
            for _ in range(len(q)): 
                i,j = q.popleft() 

                for i_off, j_off in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    r = i + i_off
                    c = j + j_off

                    if 0 <= r < rows and 0 <= c < cols and (r,c) not in visted and grid[r][c] == 1: 
                        fresh -= 1
                        grid[r][c] = 2
                        q.append((r,c))
                        visted.add((r,c))
            time += 1
        
        if fresh == 0: 
            return time 
        else: 
            return -1
                

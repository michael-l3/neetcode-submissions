from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #we check for all of the rotten fruits first and bfs
        #we have a counter of all the fresh fruit
        #if the q no longer exist and len(set) good fruit is empty then we return the time else -1 
        m = len(grid)
        n = len(grid[0])
        q = deque()
        fresh = 0
        time = 0 

        #check for all for all of the fresh fruit
        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 1: 
                    fresh += 1 
                elif grid[i][j] == 2: 
                    q.append((i,j))

        #doesnt matter if it was visted or not alr thats why we dont need set, just check around it 
        while q and fresh > 0: 
            for _ in range(len(q)): 
                i,j = q.popleft() 
                
                #check spots around it 
                for i_off,j_off in [(1,0),(-1,0),(0,-1),(0,1)]: 
                    r = i + i_off
                    c = j + j_off 

                    if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1: 
                        continue 
                    
                    grid[r][c] = 2
                    fresh -= 1
                    q.append((r, c))

            time += 1

        if fresh == 0: 
            return time
        else: 
            return -1


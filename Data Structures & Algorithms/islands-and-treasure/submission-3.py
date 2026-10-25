from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #we will get all of the points with the treasure and add it to queue
        row = len(grid)
        col = len(grid[0])
        q = deque() 
        visted = set()

        for i in range(row): 
            for j in range(col): 
                if grid[i][j] == 0: 
                    q.append((i,j))
                    visted.add((i,j))

        #now we will bfs our way out while keeping track of dist 
        dist = 0 
        while q: 
            for _ in range(len(q)): 
                i,j = q.popleft() 
                grid[i][j] = dist 

                #check around now 
                for i_off,j_off in [(1,0),(-1,0),(0,1),(0,-1)]: 
                    r = i + i_off 
                    c = j + j_off

                    #check if in bounds 
                    if 0 <= r < row and 0 <= c < col and grid[r][c] != -1 and (r,c) not in visted: 
                        q.append((r,c))
                        visted.add((r,c))
                        

            dist += 1 

             
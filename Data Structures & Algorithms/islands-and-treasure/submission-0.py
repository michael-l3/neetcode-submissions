from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #start from each of the treasures and branch out using bfs 
        row = len(grid)
        col = len(grid[0])
        q = deque() 
        visted = set()  #this is so that we dont revist the same point 

        
        #this is how we are going to start the q by adding all of the treasures in it first
        for i in range(row): 
            for j in range(col): 
                if grid[i][j] == 0: 
                    q.append((i,j))
                    visted.add((i,j))
        
        dist = 0
        while q:
            for _ in range(len(q)): 
                #first iteration it just equal the distance of itself so we dont wanna change it bc we alr at treasure 
                i,j = q.popleft() 
                grid[i][j] = dist 
                #now we have to check around that point
                for i_off,j_off in [(-1,0),(1,0),(0,-1),(0,1)]: 
                    r = i + i_off
                    c = j + j_off 

                    if r < 0 or r >= row or c < 0 or c >= col or (r,c) in visted or grid[r][c] == -1: 
                        continue 
                    else: 
                        q.append((r,c))
                        visted.add((r,c))
            dist += 1       



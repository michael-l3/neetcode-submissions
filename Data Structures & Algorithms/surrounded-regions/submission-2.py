from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #so we first need to find out what cells are safe because if it is somehow connected to an outer bound 
        #edge then it can be consider safe, everything else later will become a 'X' 
        rows = len(board)
        cols = len(board[0])
        q = deque() 

        #first we need to grab all of the "O" from the outer edges bc anything connected to those will be safe 
        #for rows
        for i in range(rows): 
            if board[i][0] == "O": 
                q.append((i,0))
            if cols > 1 and board[i][cols-1] == "O": 
                q.append((i,cols-1))
        
        #for columns 
        for j in range(1,cols-1): 
            if board[0][j] == "O": 
                q.append((0,j))
            if rows > 1 and board[rows-1][j] == "O": 
                q.append((rows-1,j))
        
        while q: 
            for _ in range(len(q)): 
                i,j = q.popleft()
                board[i][j] = 'S'

                #now we check around 
                for i_off, j_off in [(0,1),(0,-1),(1,0),(-1,0)]: 
                    r = i + i_off 
                    c = j + j_off 

                    if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O": 
                        q.append((r,c))

        #so now we have all the safe points 
        for i in range(rows): 
            for j in range(cols): 
                if board[i][j] == 'O': 
                    board[i][j] = 'X'
                elif board[i][j] == 'S': 
                    board[i][j] = 'O'
 




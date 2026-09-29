from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        q = deque() 

        #first we need to grab all of the "O" from the outer edges bc anything connected to those will be safe 
        #for rows
        for i in range(m): 
            if board[i][0] == "O": 
                q.append((i,0))
            if n > 1 and board[i][n-1] == "O": 
                q.append((i,n-1))
        
        #for columns 
        for j in range(1,n-1): 
            if board[0][j] == "O": 
                q.append((0,j))
            if m > 1 and board[m-1][j] == "O": 
                q.append((m-1,j))
        
        while q: 
            #points
            i,j = q.popleft() 
            #make everything connected to these safe 
            board[i][j] = "S"
            #now around it 
            for i_off, j_off in [(0,1),(0,-1),(1,0),(-1,0)]: 
                r = i + i_off 
                c = j + j_off 

                if r >= 0 and r < m and c >= 0 and c < n and board[r][c] == "O": 
                    q.append((r,c))

        for i in range(m): 
            for j in range(n): 
                if board[i][j] == "S": 
                    board[i][j] = "O"
                elif board[i][j] == "O": 
                    board[i][j] = "X"
            



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def dfs(i,j,index): 
            if index == len(word)-1: 
                return True
            #we dont want to reuse the letter so we keep temp 
            temp = board[i][j]
            board[i][j] = '#'

            #check around now 
            for i_off,j_off in [(1,0),(-1,0),(0,1),(0,-1)]: 
                r = i + i_off 
                c = j + j_off 

                if 0 <= r < row and 0 <= c < col and board[r][c] == word[index + 1]: 
                    if dfs(r,c,index+1): 
                        return True 
            
            #otherwise it doesnt work 
            board[i][j] = temp 
            return False


        for i in range(row): 
            for j in range(col): 
                if board[i][j] == word[0]: 
                    if dfs(i,j,0): 
                        return True 
        
        return False 
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #number of rows 
        m = len(board)
        #number columns: 
        n = len(board[0])

        def dfs(pos, index): 
            #unpack the index 
            i,j = pos 
            
            #if it isnt equal to the word at the index then it is false 
            if board[i][j] != word[index]: 
                return False 

            if index == len(word) - 1: 
                return True 
            
            if index >= len(word): 
                return False 
            
            #place holder 
            temp = board[i][j]
            board[i][j] = '#' 

            for i_off, j_off in [(1,0),(-1,0),(0,1),(0,-1)]: 
                r = i + i_off 
                c = j + j_off 

                if 0 <= r < m and 0 <= c < n: 
                    if dfs((r,c), index + 1): 
                        return True 
            
            board[i][j] = temp 
            return False 

        for i in range(m): 
            for j in range(n): 
                if board[i][j] == word[0]: 
                    if dfs((i,j), 0): 
                        return True 
    
        return False 
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board) # rows 
        n = len(board[0]) # of columns
        lenWord = len(word)
        
        if len(board) == 1 and len(word) == 1: 
            if board[0][0] == word[0]: 
                return True

        def dfs(pos, index): 
            #unpack the position 
            i,j = pos
            #case that it is correct when index = # of characters in the worwd 
            if index == lenWord: 
                return True 
            if board[i][j] != word[index]: 
                return False 
            #hold a temp character and change the character to # 
            #so that if we dfs up down left right that we wont run into the same characters twice 
            temp = board[i][j]
            board[i][j] = '#'

            #now we check around the characters 
            for i_off, j_off in [(0,1),(0,-1),(1,0),(-1,0)]: 
                r = i + i_off  #new row
                c = j + j_off  #new column

                #now we got to make sure that r and c are in bounds 
                if 0 <= r < m and 0 <= c < n: 
                    if dfs((r,c), index + 1): 
                        return True 
            
            #if we dont get the letter we want from the new rows and columns return the letter back 
            board[i][j] = temp 
            return False

        #will need to iterate the board and start once we hit the first letter of the word 
        #start the backtracking function once we hit the first letter 
        for i in range(m): 
            for j in range(n): 
                if board[i][j] == word[0]: 
                    if dfs((i,j),0): 
                        return True 
        return False


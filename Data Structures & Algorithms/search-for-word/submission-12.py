class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #return true or false here 
        #will iterate through, when it reaches the first character of word then we start dfs and look around
        #make sure that everything is in bound
        m = len(board)
        n = len(board[0])
        wordLength = len(word)

        if len(board) == 1 and len(word) == 1: 
            if board[0][0] == word[0]: 
                return True

        def dfs(pos, index): 
            i,j = pos 
            #now we have to make the function, have to make this position == '#' just in case it revisits 
            if index == wordLength: 
                return True 
            
            if board[i][j] != word[index]: 
                return False 
            #temp character 
            char = board[i][j]
            board[i][j] = '#'  #-> temp in case that we have to dfs back up 

            #now we create bounds around 
            for i_off,j_off in [(0,-1),(0,1),(-1,0),(1,0)]: 
                r = i + i_off 
                c = j + j_off

                #check boundaries 
                if 0 <= r < m and 0 <= c < n: 
                    if dfs((r,c),index + 1): 
                        return True
            
            board[i][j] = char 
            return False


        #initate by iterating, start the dfs when we reach the first character of the word
        for i in range(m): 
            for j in range(n): 
                if board[i][j] == word[0]: 
                    if dfs((i,j),0): 
                        return True
        
        return False 
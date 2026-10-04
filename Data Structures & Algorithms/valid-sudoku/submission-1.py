class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #probably use a set in ordker to check each col, row, and box 

        #validate row 
        for i in range(9):
            s = set() 
            for j in range(9):
                item = board[i][j]
                if item in s: 
                    return False 
                elif item != ".": 
                    s.add(item)

        #validate column 
        for i in range(9):
            s = set() 
            for j in range(9):
                item = board[j][i]
                if item in s: 
                    return False 
                elif item != ".": 
                    s.add(item)

        #validate the box
        starts = [(0,0),(3,0),(6,0),
        (0,3),(3,3),(6,3),(0,6),(3,6),(6,6)]

        for row,col in starts: 
            s = set() 
            for i in range(row,row+3): 
                for j in range(col,col+3): 
                    item = board[i][j]
                    if item in s: 
                        return False 
                    elif item != ".": 
                        s.add(item)
        
        return True


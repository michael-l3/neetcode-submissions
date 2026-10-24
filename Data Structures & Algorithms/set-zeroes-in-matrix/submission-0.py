class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        
        zero_rows = set()
        zero_cols = set()
        
        # Pass 1: Record which rows and columns have a zero
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
                    
        # Pass 2: Apply the zeros
        for r in range(rows):
            for c in range(cols):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        r = len(matrix) * len(matrix[0]) - 1

        #we flatten the grid so that we can do the binary search 

        while l <= r: 
            mid = (l+r) // 2 
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] > target: 
                r = mid - 1
            elif matrix[row][col] < target: 
                l = mid + 1 
            else:
                if matrix[row][col] == target: 
                    return True 
        
        return False
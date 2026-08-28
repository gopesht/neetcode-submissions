class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        i, j = 0, len(matrix) - 1

        while i <= j:
            m = (i + j) // 2
            if matrix[m][n-1] < target:
                i = m + 1
            elif matrix[m][0] > target:
                j = m - 1
            else: 
                break
            
        if not (i<=j):
            return False
        
        row = (i+j)//2

        i, j = 0, len(matrix[0])

        while i <= j:
            m = (i+j) // 2
            if matrix[row][m] > target:
                j = m - 1
            elif matrix[row][m] < target:
                i = m+1
            else: 
                return True
        return False


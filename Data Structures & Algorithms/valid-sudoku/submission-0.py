class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                row_set = rows[i]
                col_set = cols[j]
                square_set = squares[((int(i/3) * 3) + int(j/3))]
                if board[i][j] in row_set:
                    return False
                if board[i][j] in col_set:
                    return False
                if board[i][j] in square_set:
                    return False
                if board[i][j] != ".":
                    row_set.add(board[i][j])
                    col_set.add(board[i][j])
                    square_set.add(board[i][j])
        

        return True
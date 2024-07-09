def isValidSudoku(board: list[list[str]]) -> bool:
    # keep a dict as list of location of nos. as [row, column, 3*3 subunit]
    d = {str(x): [] for x in range(1, 10)}
    for i in range(9):
        for j in range(9):
            # if no. exists in dict, check if its valid
            if board[i][j] != '.' and d[board[i][j]]:
                for val in d[board[i][j]]:
                    if i == val[0] or j == val[1] or (i//3, j//3) == val[2]:
                        return False
            # if no. doesn't exist in dict or it exists but is valid, add its location
            if board[i][j] != '.':
                d[board[i][j]].append([i, j, (i//3, j//3)])
    return True

board = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))

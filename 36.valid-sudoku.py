#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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
    
# @lc code=end


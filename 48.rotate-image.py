#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #for each layer, use exchange 4 corners and do this for the first row
        #indexing is tricky, probably should've done for i in range(l, n-l):
        n = len(matrix[0])
        for l in range(n // 2):
            for i in range(n-1-2*l):
                matrix[l][i+l], matrix[i+l][n-1-l] = matrix[i+l][n-1-l], matrix[l][i+l]
                matrix[l][i+l], matrix[n-1-l][n-1-i-l] = matrix[n-1-l][n-1-i-l], matrix[l][i+l]
                matrix[l][i+l], matrix[n-1-i-l][l] = matrix[n-1-i-l][l], matrix[l][i+l]
        
# @lc code=end


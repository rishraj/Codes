class Solution:
    def rotate (self, matrix: list[list[int]]) -> None:
        #for each layer, use exchange 4 corners and do this for the first row
        #indexing is tricky, probably should've done for i in range(l, n-l):
        n = len(matrix[0])
        for l in range(n // 2):
            for i in range(n-1-2*l):
                matrix[l][i+l], matrix[i+l][n-1-l] = matrix[i+l][n-1-l], matrix[l][i+l]
                matrix[l][i+l], matrix[n-1-l][n-1-i-l] = matrix[n-1-l][n-1-i-l], matrix[l][i+l]
                matrix[l][i+l], matrix[n-1-i-l][l] = matrix[n-1-i-l][l], matrix[l][i+l]
    
n = int(input("Enter size of array\n"))
matrix = [[0]*n for i in range(n)]
print("Enter the matrix row-wise")
for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input())

Solution().rotate(matrix)

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print("\n")
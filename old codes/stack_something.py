def is_safe(n, i, j):
    return (i>=0) and (i<n) and (j>=0) and (j<3)

def my_func(i, j, n, mat, visited, res, stack):
    if len(stack) == n:
        res.append(stack)
        return
    if not visited[i][j]:
        visited[i][j] = True
        if is_safe(n, i+1, 0):
            my_func(i+1, 0, n, mat, visited, res, stack+(mat[i+1][0]))
        if is_safe(n, i+1, 1):
            my_func(i+1, 1, n, mat, visited, res, stack+(mat[i+1][1]))
        if is_safe(n, i+1, 2):
            my_func(i+1, 2, n, mat, visited, res, stack+(mat[i+1][2]))
        visited[i][j] = False


n = list(x for x in input().strip())
# print(n)
mat = [[0 for x in range(3)] for y in range(len(n))]
for i in range(len(n)):
    if n[i] == '2':
        mat[i][0] = 'A'
        mat[i][1] = 'B'
        mat[i][2] = 'C'
    elif n[i] == '3':
        mat[i][0] = 'D'
        mat[i][1] = 'E'
        mat[i][2] = 'F'
    elif n[i] == '4':
        mat[i][0] = 'G'
        mat[i][1] = 'H'
        mat[i][2] = 'I'
    elif n[i] == '5':
        mat[i][0] = 'J'
        mat[i][1] = 'K'
        mat[i][2] = 'L'
    elif n[i] == '6':
        mat[i][0] = 'M'
        mat[i][1] = 'N'
        mat[i][2] = 'O'
    elif n[i] == '7':
        mat[i][0] = 'P'
        mat[i][1] = 'R'
        mat[i][2] = 'S'
    elif n[i] == '8':
        mat[i][0] = 'T'
        mat[i][1] = 'U'
        mat[i][2] = 'V'
    elif n[i] == '9':
        mat[i][0] = 'W'
        mat[i][1] = 'X'
        mat[i][2] = 'Y'

visited = [[False for x in range(3)] for y in range(len(n))]
res = []
my_func(0, 0, len(n), mat, visited, res, str(mat[0][0]))
my_func(0, 1, len(n), mat, visited, res, str(mat[0][1]))
my_func(0, 2, len(n), mat, visited, res, str(mat[0][2]))

print(res)
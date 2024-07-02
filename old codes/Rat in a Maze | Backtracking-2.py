def isSafe(arr, n, x, y):
    return x >= 0 and x < n and y >= 0 and y < n and (arr[x][y] == 1)


def printArray(A, m):
    for i in range(m):
        for j in range(m):
            print(A[i][j], end=' ')
        print()


def findPathUtil(arr, n, results, curr_str, row, col, vis):
    if row == n - 1 and col == n - 1:
        results.append(curr_str)
        return
    if vis[row][col] == 1:
        return
    vis[row][col] = 1
    if isSafe(arr, n, row + 1, col):
        findPathUtil(arr, n, results, curr_str + 'D', row + 1, col, vis)
    if isSafe(arr, n, row - 1, col):
        findPathUtil(arr, n, results, curr_str + 'U', row - 1, col, vis)
    if isSafe(arr, n, row, col + 1):
        findPathUtil(arr, n, results, curr_str + 'R', row, col + 1, vis)
    if isSafe(arr, n, row, col - 1):
        findPathUtil(arr, n, results, curr_str + 'L', row, col - 1, vis)
    vis[row][col] = 0


def findPath(arr, n):
    vis = [[0 for i in range(n)] for j in range(n)]
    results = []
    findPathUtil(arr, n, results, '', 0, 0, vis)
    results.sort()
    return (' '.join(results))

for i in range(int(input())):
    n = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    matrix = [[0 for i in range(n[0])]for j in range(n[0])]
    k=0
    for i in range(n[0]):
        for j in range(n[0]):
            matrix[i][j] = arr[k]
            k+=1
    print(findPath(matrix, n[0]))
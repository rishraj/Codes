def isSafe(maze, n, x, y):
    return (x>=0) and (x<n) and (y>=0) and (y<n) and (maze[x][y]!=0)

def my_func_util(maze, n, row, col, sol):
    if row == n-1 and col == n-1:
        sol[n-1][n-1] = 1
        return True
    if isSafe(maze, n, row, col):
        if sol[row][col] == 1:
            return False
        sol[row][col] = 1
        for i in range(min(maze[row][col], n)):
            if my_func_util(maze, n, row, col+i+1, sol):
                return True
            if my_func_util(maze, n, row+i+1, col, sol):
                return True
        sol[row][col] = 0
    return False


def my_func(maze, n):
    sol = [[0 for x in range(n)] for y in range(n)]
    if my_func_util(maze, n, 0, 0, sol):
        for i in range(n):
            for j in range(n):
                print(sol[i][j], end = ' ')
            print('')
    else:
        print('-1')


for _ in range(int(input())):
    n  = int(input())
    maze = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        arr = list(int(x) for x in input().split())
        for j in range(n):
            maze[i][j] = arr[j]
    my_func(maze, n)
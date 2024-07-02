
def is_safe(x, y, n, sol):
    return (x>=0)and(x<n)and(y>=0)and(y<n)and(sol[x][y]==-1)

def solve_ktUTIL(x, y, n, move, sol, movei):
    if movei==(n*n):
        return True
    for i in range(n):
        for j in range(n):
            print(sol[i][j], end=' ')
        print()
    print('------------------------------')
    if sol[x][y] > -1:
        return False

    sol[x][y] = movei
    for i in range(8):
        xmove = x + move[i][0]
        ymove = y + move[i][1]
        if is_safe(xmove, ymove, n, sol):
            if solve_ktUTIL(xmove, ymove, n, move, sol, movei+1)==True:
                return True
    sol[x][y] = -1
    return False

def solve_kt():
    n = 8
    x = 0
    y = 0
    move = [[1, 2], [2, 1], [1, -2], [-2, 1], [-1, 2], [2, -1], [-1, -2], [-2, -1]]
    sol = [[-1 for x in range(n)] for y in range(n)]
    movei = 0
    # sol[0][0] = 0
    solve_ktUTIL(x, y, n, move, sol, movei)
    for i in range(n):
        for j in range(n):
            print(sol[i][j], end=' ')
        print()

solve_kt()

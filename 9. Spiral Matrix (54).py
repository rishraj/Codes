def spiralOrder(matrix: list[list[int]]) -> list[int]:
    # keep 4 boundaries for top, right, bottom, left
    t, r, b, l = 0, len(matrix[0]) - 1, len(matrix) - 1, 0
    # flag is to tell which direction to go
    flag, res = 0, []
    while t <= b and r >= l:
        if not flag:
            for i in range(l, r+1):
                res.append(matrix[t][i])
            t += 1
        elif flag == 1:
            for i in range(t, b+1):
                res.append(matrix[i][r])
            r -= 1
        elif flag == 2:
            for i in range(r, l-1, -1):
                res.append(matrix[b][i])
            b -= 1
        else:
            for i in range(b, t-1, -1):
                res.append(matrix[i][l])
            l += 1
        flag = (flag + 1) % 4
    return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))
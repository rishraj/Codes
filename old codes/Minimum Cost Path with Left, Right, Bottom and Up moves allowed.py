def minimum(distance, visited):
    m = float('inf')
    a = [-1, -1]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and distance[i][j] < m:
                m = distance[i][j]
                a[0] = i
                a[1] = j
    return m, a

def my_func(mat, n):
    distance = [[float('inf') for x in range(n)] for y in range(n)]
    distance[0][0] = mat[0][0]
    visited = [[False for x in range(n)] for y in range(n)]
    count = 0
    while count < n*n:
        m, a = minimum(distance, visited)
        count += 1
        visited[a[0]][a[1]] = True
        if a[0] < n-1 and distance[a[0]][a[1]] + mat[a[0]+1][a[1]] < distance[a[0]+1][a[1]]:
            distance[a[0] + 1][a[1]] = distance[a[0]][a[1]] + mat[a[0]+1][a[1]]
        if a[0] > 0 and distance[a[0]][a[1]] + mat[a[0]-1][a[1]] < distance[a[0]-1][a[1]]:
            distance[a[0] - 1][a[1]] = distance[a[0]][a[1]] + mat[a[0]-1][a[1]]
        if a[1] < n-1 and distance[a[0]][a[1]] + mat[a[0]][a[1]+1] < distance[a[0]][a[1]+1]:
            distance[a[0]][a[1]+1] = distance[a[0]][a[1]] + mat[a[0]][a[1]+1]
        if a[1] > 0 and distance[a[0]][a[1]] + mat[a[0]][a[1]-1] < distance[a[0]][a[1]-1]:
            distance[a[0]][a[1]-1] = distance[a[0]][a[1]] + mat[a[0]][a[1]-1]
    print(distance[n-1][n-1])



for _ in range(int(input())):
    n = int(input())
    mat = [[0 for x in range(n)] for y in range(n)]
    k = 0
    arr = list(int(x) for x in input().split())
    for i in range(n):
        for j in range(n):
            mat[i][j] = arr[k]
            k += 1
    # print(mat)
    my_func(mat, n)

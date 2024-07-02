n = int(input("Enter the number of items: "))

print("Enter the weights")
wt = []
for i in range(n):
    wt.append(int(input()))
print("Enter the values")
val = []
for i in range(n):
    val.append(int(input()))
max_wt = int(input("Enter the max. weight: "))


# ----------------Bottom up approach--------------------------
arr = [[0 for x in range(max_wt+1)] for y in range(n+1)]

for i in range(n+1):
    for j in range(max_wt+1):
        if i == 0 or j == 0:
            arr[i][j] = 0
        elif wt[i-1] <= j:
            arr[i][j] = max(arr[i-1][j], arr[i-1][j-wt[i-1]]+val[i-1])
        elif j < wt[i-1]:
            arr[i][j] = arr[i-1][j]
print(arr[n][max_wt])
# ------------------------------------------------------------

# ---------------Top down approach----------------------------
m = [[-1 for x in range(max_wt+1)] for y in range(n+1)]


def top_down(val, wt, i, j, m):
    if m[i][j] >= 0:
        return m[i][j]
    if i == 0 or j == 0:
        m[i][j] = 0
    elif j >= wt[i-1]:
        m[i][j] = max(top_down(val, wt, i-1, j, m), top_down(val, wt, i-1, j-wt[i-1], m)+val[i-1])
    elif j < wt[i-1]:
        m[i][j] = top_down(val, wt, i-1, j, m)
    return m[i][j]


print(top_down(val, wt, n, max_wt, m))
# ------------------------------------------------------------





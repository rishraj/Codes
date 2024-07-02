n = int(input("Enter the number of denominations: "))
print("Enter the denominations in ascending order")
t = []
for i in range(n):
    t.append(int(input()))
x = int(input("Enter the amount: "))
arr = [-1 for _ in range(x+1)]
arr[0] = 0
for i in range(1, x+1):
    if i in t:
        arr[i] = 1
    else:
        j = 0
        min_val = 10000
        while t[j] < i and j < len(t)-1:
            min_val = min(min_val, arr[i-t[j]]+1)
            j += 1
        arr[i] = min_val
    # print("arr[", i, "] = ", arr[i])
print(arr[x])

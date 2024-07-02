n = int(input("Enter the size of the array: "))
print("Enter the numbers:")
arr = []
for i in range(n):
    arr.append(int(input()))


max_sub_length = [1]
for i in range(1, len(arr)):
    max_length = 0
    visited = False
    for j in range(i):
        if arr[i] > arr[j] and max_sub_length[j]+1 > max_length:
            visited = True
            max_length = max_sub_length[j]+1
    if visited:
        max_sub_length.append(max_length)
    else:
        max_sub_length.append(1)

print(max_sub_length[n-1])

def swap(a, b):
    return b, a


n = int(input('Enter the size of the array: '))
print("Enter the elements of the array:")
arr = []
for i in range(n):
    arr.append(int(input()))

for i in range(0, n-1):
    if i%2 == 0 and arr[i] > arr[i+1]:
        arr[i], arr[i+1] = swap(arr[i], arr[i+1])
    elif i%2 == 1 and arr[i] < arr[i+1]:
        arr[i], arr[i+1] = swap(arr[i], arr[i+1])

print(arr)

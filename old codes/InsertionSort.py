def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while arr[j] > key and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


n = int(input("Enter the size of the array: "))
arr = []
print("Enter the elements of the array")
for i in range(n):
    arr.append(int(input()))

insertion_sort(arr)
print(arr)

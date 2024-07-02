def binary_search(arr, p, q, key):
    if p > q:
        print("Element not found")
        return -1
    m = int((p+q)/2)
    if arr[m] == key:
        return m
    elif arr[m] > key:
        return binary_search(arr, p, m-1, key)
    elif arr[m] < key:
        return binary_search(arr, m+1, q, key)


n = int(input("Enter the size of array: "))
print("Enter the elements of the array:")
arr = []
for i in range(n):
    arr.append(int(input()))
key = int(input("Enter the element to be searched: "))

print(binary_search(arr, 0, n-1, key))
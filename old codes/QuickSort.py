def partition(arr, p, r):
    i = p-1
    for j in range(p, r):
        if arr[j] < arr[r]:
            arr[i+1], arr[j] = swap(arr[i+1], arr[j])
            i += 1
    arr[i+1], arr[r] = swap(arr[i+1], arr[r])
    return i+1


def swap(a, b):
    return b, a


def quicksort(arr, p, r):
    if p >= r:
        return
    q = partition(arr, p, r)
    quicksort(arr, p, q-1)
    quicksort(arr, q+1, r)


n = int(input("Enter the size of the array: "))
arr = []
print("Enter the elements of the array")
for i in range(n):
    arr.append(int(input()))

quicksort(arr, 0, n-1)
print(arr)

def merge(arr, p, r, q):
    arr1 = []
    arr2 = []
    for i in range(p, r+1):
        arr1.append(arr[i])
    for i in range(r+1, q+1):
        arr2.append(arr[i])
    arr1.append(10000)
    arr2.append(10000)
    j = 0
    k = 0
    for i in range(len(arr1)+len(arr2)-2):
        if arr1[j] < arr2[k]:
            arr[p+i] = arr1[j]
            j += 1
        else:
            arr[p+i] = arr2[k]
            k += 1


def mergesort(arr, p, q):
    if p >= q:
        return
    else:
        r = int((p+q)/2)
        mergesort(arr, p, r)
        mergesort(arr, r+1, q)
        merge(arr, p, r, q)


n = int(input("Enter the size of the array: "))
arr = []
print("Enter the elements of the array")
for i in range(n):
    arr.append(int(input()))

mergesort(arr, 0, n-1)
print(arr)

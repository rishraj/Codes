def triplets(arr, sum):
    total = 0
    for i in range(n-2):
        j = i+1
        k = n-1
        while j < k:
            if arr[i]+arr[j]+arr[k] >= sum:
                k = k-1
            else:
                total = total + (k-j)
                j += 1
    print(total)


n = int(input("Enter the size of the array: "))
print("Enter the elements")
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

sum = int(input("Enter the sum: "))

triplets(arr, sum)
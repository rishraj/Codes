import random

def bubble_sort(arr, n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    for i in range(n):
        print(arr[i], end=' ')

n = random.randint(1, 15)
arr = []
for i in range(n):
    arr.append(random.randint(1, 100))
print(arr)
bubble_sort(arr, n)
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     bubble_sort(arr, n)
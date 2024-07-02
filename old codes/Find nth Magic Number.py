from collections import deque

def bits_conversion(arr, n):
    if n != 0:
        q = int(n/2)
        r = n%2
        arr.append(r)
        bits_conversion(arr, q)

n = int(input('Enter the number: '))
arr = deque()
bits_conversion(arr, n)
# print(arr)
sum = 0
for i in range(len(arr)-1, -1, -1):
    sum = sum+(arr[i]*pow(5, i+1))

print(sum)
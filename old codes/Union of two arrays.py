def myfunc(arr1, arr2, arr3, n1, n2, n3):
    i = 0
    j = 0
    k = 0
    count = 0
    res = []
    while j < n2 and i < n1 and k < n3:
        # print(arr1[i], arr2[j], arr3[k])
        temp = min(arr1[i], arr2[j], arr3[k])
        if arr1[i] == arr2[j] and arr1[i] == arr3[k]:
            res.append(arr1[i])
            count += 1
            i += 1
            j += 1
            k += 1
        elif arr1[i] == temp:
            i += 1
        elif arr2[j] == temp:
            j += 1
        elif arr3[k] == temp:
            k += 1
    res = set(res)
    if count == 0:
        print('-1')
    else:
        for i in res:
            print(i, end=' ')
        print('')


t = int(input())
for _ in range(t):
    n1, n2, n3 = (int(x) for x in input().split())
    arr1 = list(int(x) for x in input().split())
    arr2 = list(int(x) for x in input().split())
    arr3 = list(int(x) for x in input().split())
    myfunc(arr1, arr2, arr3 ,n1, n2, n3)
def my_func(arr, n):
    my_dict = {}
    for i in range(n):
        my_dict[arr[0][i]] = arr[0][i]
    # print('my_dict = ', my_dict)
    for i in range(1, n):
        temp = {}
        for j in range(n):
            temp[arr[i][j]] = arr[i][j]
        # print('temp = ', temp)
        remove_key = []
        for key in my_dict.keys():
            # print('key = ', key)
            if key not in temp:
                # print('hurray')
                remove_key.append(key)
        # print(remove_key)
        for key in remove_key:
            if key in my_dict:
                del my_dict[key]
    return len(my_dict)


t = int(input())
res = []
for _ in range(t):
    n = int(input())
    a = list(int(x) for x in input().split())
    arr = [[0 for x in range(n)] for y in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            arr[i][j] = a[k]
            k += 1
    res.append(my_func(arr, n))
print(*res)

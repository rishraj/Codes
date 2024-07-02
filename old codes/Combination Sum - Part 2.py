def my_func(arr, n, s):
    stack = []
    results = []
    my_util(arr ,n ,s, 0, stack, results)
    # print(results)
    if len(results) == 0:
        print('Empty')
    else:
        for result in results:
            print(result.replace('[', '(').replace(']', ')').replace(',', ''), end='')
        print('')

def my_util(arr, n, s, i, stack, results):
    if sum(stack) == s:
        if str(stack) not in results:
            results.append(str(stack))
        return
    if sum(stack) > s or i>=n:
        return
    stack.append(arr[i])
    my_util(arr, n, s, i+1, stack, results)
    stack.pop()
    my_util(arr, n, s, i+1, stack, results)


for _ in range(int(input())):
    n = int(input())
    arr = list(int(x) for x in input().split())
    arr = sorted(arr)
    # print(arr)
    s = int(input())
    my_func(arr, n, s)

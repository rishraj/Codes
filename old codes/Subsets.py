def my_func(arr, n):
    stack = []
    results = []
    i = 0
    my_util(arr, n, i, stack, results)
    for result in results:
        print(result.replace('[', '(').replace(']', ')').replace(',', ''), end='')
    print('')

def my_util(arr, n, i, stack, results):
    if str(stack) not in results:
        results.append(str(stack))
    if i>=n:
        return
    stack.append(arr[i])
    my_util(arr, n, i+1, stack, results)
    stack.pop()
    my_util(arr, n, i+1, stack, results)


for _ in range(int(input())):
    n = int(input())
    arr = list(int(x) for x in input().split())
    arr = sorted(arr)
    my_func(arr, n)
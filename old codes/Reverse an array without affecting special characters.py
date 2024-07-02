str = input()
stack = list()

for i in range(len(str)):
    if str[i].isalpha():
        stack.append(str[i])

for i in range(len(str)):
    if str[i].isalpha():
        print(stack.pop(), end='')
    else:
        print(str[i], end='')
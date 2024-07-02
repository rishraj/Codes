from collections import defaultdict

for _ in range(int(input())):
    s = input()
    d = defaultdict(int)
    X = 0
    Y = 0
    for c in s:
        d[c] += 1
    for key in d.keys():
        if ord(key)%2 == 0 and d[key]%2 == 0:
            X += 1
        elif ord(key)%2 == 1 and d[key]%2 == 1:
            Y += 1
    if (X+Y)%2 == 0:
        print('EVEN')
    else:
        print('ODD')

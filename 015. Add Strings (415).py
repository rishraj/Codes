def addStrings(num1: str, num2: str) -> str:
    c = 0
    r = ''
    while num1 or num2 or c:
        if num1 and num2:
            s = (ord(num1[-1]) - ord('0')) + (ord(num2[-1]) - ord('0')) + c
            r = str(s % 10) + r
            c = s // 10
            num1 = num1[:-1]
            num2 = num2[:-1]
        elif num1:
            s = (ord(num1[-1]) - ord('0')) + c
            r = str(s % 10) + r
            c = s // 10
            num1 = num1[:-1]
        elif num2:
            s = (ord(num2[-1]) - ord('0')) + c
            r = str(s % 10) + r
            c = s // 10
            num2 = num2[:-1]
        elif c:
            r = str(c) + r
            break
    return r
    
    
num1 = "1"
num2 = "9"
print(addStrings(num1, num2))
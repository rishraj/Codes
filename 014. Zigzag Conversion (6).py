def convert(s: str, numRows: int) -> str:
    # my code (needless complexities)
    """ if numRows == 1:
        return s
    i, j, flag, res = 1, 1, 0, ''
    res_list = [[] for _ in range(numRows)]
    res_list[0].append(s[0])
    while j < len(s):
        if not flag:
            if i <= numRows - 1:
                res_list[i].append(s[j])
                i += 1
                j += 1
                continue
            i -= 2
            flag = 1
        if flag:
            if i >= 0:
                res_list[i].append(s[j])
                i -= 1
                j += 1
                continue
            i += 2
            flag = 0
    for i in res_list:
        res += "".join(i)
    return res """

    # leetcode soln. (difference = add element first, increment or decrement later)
    if numRows == 1:
        return s
    rows = [""] * numRows # empty list of strings
    i = 0 # to fluctuate btw rows
    inc = 1 # to increase or decrease i
    for c in s:
        rows[i] += c
        if i == 0:
            inc = 1
        elif i == numRows - 1:
            inc = -1
        i += inc
    return "".join(rows)
    
    
s = "PAYPALISHIRING"
numRows = 4
print(convert(s, numRows))
def longestPalindrome(s: str) -> int:
    res, flag, d = 0, 0, {}
    for ch in s:
        d[ch] = d.get(ch, 0) + 1
    for key in d:
        if not d[key] % 2:
            res += d[key]
        else:
            flag = 1
            res += d[key] - 1
    if flag:
        return res + 1
    return res

s = "abccccdd"
print(longestPalindrome(s))
        
        
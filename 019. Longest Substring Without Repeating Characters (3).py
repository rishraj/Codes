def lengthOfLongestSubstring(s: str) -> int:
    res, l, r, s_set = 0, 0, 0, set()
    while r < len(s):
        if s[r] in s_set:
            while s[r] in s_set:
                s_set.remove(s[l])
                l += 1
        s_set.add(s[r])
        r += 1
        res = max(res, r - l) # don't use len(s_set) instead of r - l, it increases time
    return res
    
    
s = "pwwkew"
print(lengthOfLongestSubstring(s))
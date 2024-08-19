#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
        
# @lc code=end


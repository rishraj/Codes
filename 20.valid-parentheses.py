#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # an easy stack problem
        stack = []
        d = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in d:
                if stack:
                    if d[ch] == stack[-1]: stack.pop()
                    else: return False
                else: return False
            else: stack.append(ch)
        return True if not stack else False
    
# @lc code=end


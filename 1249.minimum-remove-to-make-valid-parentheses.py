#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # rem = stores index of chars to be removed
        # stack = stores index of '('
        # res = to build the result string
        rem, stack, res = [], [], ''
        for i in range(len(s)):
            if s[i] == '(': stack.append(i)
            elif s[i] == ')' and stack: stack.pop() # if ')' and stack not empty, pop the last '(' index
            elif s[i] == ')' and not stack: rem.append(i)
        rem += stack # add unclosed '(' indices to be removed
        rem = set(rem) # for constant lookup time
        for i in range(len(s)):
            if i not in rem: res += s[i]
        return res
    
# @lc code=end


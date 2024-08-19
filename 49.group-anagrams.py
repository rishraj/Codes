#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # instead of sorting, could've used a list of 26 size to indicate frequency of that character
        # time of that would've been len(strs) * max_len(str)
        # time of below code is len(strs) * (max_len(str) * log(max_len(str))) coz of sorting
        
        d = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in d:
                d[sorted_s].append(s)
            else:
                d[sorted_s] = [s]
                
        return [x for x in d.values()]

        
# @lc code=end


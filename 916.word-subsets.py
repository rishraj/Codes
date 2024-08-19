#
# @lc app=leetcode id=916 lang=python3
#
# [916] Word Subsets
#

# @lc code=start
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # combine all words2 list in a single dict; but think about how this should be done
        # for the next time, reduce size of dict d; don't need to have all alphabets as keys (see notes)
        
        """ res = []
        d = {chr(key): 0 for key in range(ord('a'), ord('z') + 1)}
        for w2 in words2:
            w2_dict = {}
            for ch in w2:
                w2_dict[ch] = w2_dict.get(ch, 0) + 1
            for key in d:
                if key in w2_dict:
                    d[key] = max(d[key], w2_dict[key])
        for w1 in words1:
            d1, flag = {}, 0
            for ch in w1:
                d1[ch] = d1.get(ch, 0) + 1
            for key in d:
                if (d[key] > 0) and (key not in d1 or d1[key] < d[key]):
                    flag = 1
                    break
            if not flag:
                res.append(w1)
        return res """
        
        #######################################################################
        # pythonic way (though slower coz of module dependencies)
        # Counter is a dict subclass to count hashable objects
        """ 
        c = Counter(a=3, b=1)
        d = Counter(a=1, b=2)
        c + d                       # add two counters together:  c[x] + d[x]
        output = Counter({'a': 4, 'b': 3})
        c - d                       # subtract (keeping only positive counts)
        output = Counter({'a': 2})
        c & d                       # intersection:  min(c[x], d[x])
        output = Counter({'a': 1, 'b': 1})
        c | d                       # union:  max(c[x], d[x])
        output = Counter({'a': 3, 'b': 2})
        c == d                      # equality:  c[x] == d[x]
        output = False
        c <= d                      # inclusion/subset:  c[x] <= d[x]
        output = False
        """
        d = reduce(lambda x, y: x | y, map(Counter, words2))
        return [w1 for w1 in words1 if Counter(w1) >= d]
    
# @lc code=end


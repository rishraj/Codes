#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # O(n^3) solution
        """ res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                cur = 0
                for z in range(i, j+1):
                    cur += nums[z]
                if cur == k:
                    res += 1
        return res """

        # O(n^2) solution = keep a running sum hashmap
        # d[i] keeps sum of nums[0] till nums[i]
        # for every continuous sub-array (a, b), its sum = d[b] - d[a]
        """ cur, res, d = 0, 0, {}
        d[-1] = 0
        for i in range(len(nums)):
            cur += nums[i]
            d[i] = cur
        for i in range(len(nums)):
            for j in range(-1, i):
                if d[i]-d[j] == k:
                    res += 1
        return res """
        
        # O(n) soln.
        # for every index i, can i remove a prefix (0, j){where j < i} such that remaining sum is k
        # sum of (0, i) - sum of (0, j){where j < i} = k --> sum of (0, j) = k - sum of (0, i)
        # Calculate sum of (0, i) using cur, find if required sum of (0, j) is present and finally,
        # store (0, i) to later use as (0, j) for some other i
        cur, res = 0, 0
        d = {0: 1} # imagine 1 empty prefix with sum = 0 (to consider entire subarray (0, i)) (otherwise nums = [2] & k = 2 fails)
        for num in nums:
            cur += num
            res += d.get(cur - k, 0)
            d[cur] = d.get(cur, 0) + 1
        return res
    
# @lc code=end


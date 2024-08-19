#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if target > numbers[l] + numbers[r]: l += 1
            elif target < numbers[l] + numbers[r]: r -= 1
            else: return [l + 1, r + 1]
            
# @lc code=end


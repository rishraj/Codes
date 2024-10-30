#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#

# @lc code=start
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # create heap
        heap = [(l[0], i, 0) for i, l in enumerate(nums)]
        heapq.heapify(heap)
        
        # tracking max with cur_max
        cur_max = max(heap)[0]
        range = [heap[0][0], cur_max]
        
        # loop would only run till len(heap) == len(nums) or it would break
        while heap:
            val, listIndex, index = heapq.heappop(heap)
            if cur_max - val < range[1] - range[0]:
                range[0], range[1] = val, cur_max
            if index + 1 < len(nums[listIndex]):
                heapq.heappush(heap, (nums[listIndex][index + 1], listIndex, index + 1))
                cur_max = max(cur_max, nums[listIndex][index + 1])
            else:
                break
        return range
        
# @lc code=end


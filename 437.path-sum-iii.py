#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # very similar to 560. Subarray Sum Equals K problem
        self.res = 0
        prefixSum = {0: 1} # 1 empty prefix with sum = 0
        def dfs(node, cur_sum):
            if not node: return
            cur_sum += node.val
            self.res += prefixSum.get(cur_sum - targetSum, 0)
            prefixSum[cur_sum] = prefixSum.get(cur_sum, 0) + 1
            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)
            prefixSum[cur_sum] -= 1 # backtracking from dict is very imp
            
        dfs(root, 0)
        return self.res
        
# @lc code=end


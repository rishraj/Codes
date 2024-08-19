#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:        
        def dfs(node, cur_sum):
            if not node: return False # null node base case
            if not node.left and not node.right: # leaf node base case
                return (cur_sum + node.val) == targetSum
            return (dfs(node.left, cur_sum + node.val) or
                dfs(node.right, cur_sum + node.val))
            
        return dfs(root, 0)
            
# @lc code=end


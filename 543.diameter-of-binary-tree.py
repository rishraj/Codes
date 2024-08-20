#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        # diameter = left subtree height + right subtree height
        # thus, write dfs to calculate height of a tree
        def dfs(node):
            if not node: return -1
            left = dfs(node.left) # height of left subtree
            right = dfs(node.right) # height of right subtree
            self.res = max(self.res, left + right + 2) # diameter of tree if including this node
            return 1 + max(left, right) # height of tree
        
        dfs(root)
        return self.res
# @lc code=end


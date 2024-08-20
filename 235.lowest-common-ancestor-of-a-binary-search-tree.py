#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val: # meaning one of them is LCA
            return root
        if min(p.val, q.val) < root.val < max(p.val, q.val): # if p and q on opposite subtrees
            return root
        if p.val < root.val: # both p and q on left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        else: # both p and q on right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        
# @lc code=end


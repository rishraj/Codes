#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """ def bst(root):
            if root.val == val:
                return root
            elif val < root.val:
                return bst(root.left) if root.left else None
            else:
                return bst(root.right) if root.right else None
        return bst(root) """
        
        # shorter code
        def bst(root):
            if not root: return None
            if val < root.val: return bst(root.left)
            elif val > root.val: return bst(root.right)
            else: return root
        return bst(root)
    
# @lc code=end


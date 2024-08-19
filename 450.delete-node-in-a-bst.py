#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def minimum(node):
            while node and node.left:
                node = node.left
            return node

        def delete(node, val):
            if not node: return None
            if val < node.val:
                node.left = delete(node.left, val)
            elif val > node.val:
                node.right = delete(node.right, val)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    minNode = minimum(node.right)
                    node.val = minNode.val
                    node.right = delete(node.right, minNode.val)
            return node
        
        return delete(root, val)
# @lc code=end


#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # below näive dfs approach fails in cases like [5,4,6,null,null,3,7]
        """ if not root: return True # null node
        return (root.left.val < root.val and self.isValidBST(root.left) and
                root.right.val > root.val and self.isValidBST(root.right)) """
        
        # brute force -> for each node, check if every value in left subtree is less than the node and
        # every value in right subtree is greater than the node.
        # this too passes on leetcode :P
        """ def helper(node, val, flag): # flag = 0 for less than
            if not node: return True
            if not flag:
                return node.val < val and helper(node.left, val, flag) and helper(node.right, val, flag)
            return node.val > val and helper(node.left, val, flag) and helper(node.right, val, flag)
            
        def bruteForce(node):
            if not node: return True
            return (helper(node.left, node.val, 0) and helper(node.right, node.val, 1) and
                    bruteForce(node.left) and bruteForce(node.right)) """
        
        # optimised -> pass allowed range of node as an argument
        def valid(node, left, right):
            if not node: return True # base case
            return (left < node.val < right) and valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, float("-inf"), float("inf"))
# @lc code=end


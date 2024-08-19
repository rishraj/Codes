#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive soln.
        """ res = [] # since list is mutable, self.res is not needed
        def helper(node):
            if not node: return
            helper(node.left)
            helper(node.right)
            res.append(node.val)
        helper(root)
        return res """
        
        # iterative soln.
        # reverse pre-order is the post-order in reverse (imp to note, otherwise postorder is difficult to implement)
        if not root: return root # edge case
        res, stack = [], [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left: stack.append(cur.left)
            if cur.right: stack.append(cur.right)
        return res[::-1]
    
# @lc code=end


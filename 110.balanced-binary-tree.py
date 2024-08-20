#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        """ # brute force (time = O(n^2)) (passes on leetcode :P)
        # top down dfs on each node to check if it is balanced
        self.height, self.res = 0, True
        
        # returns height of a tree
        def tree_height(node, cur_height):
            if not node:
                if self.height < cur_height:
                    self.height = cur_height
                return
            tree_height(node.left, cur_height + 1)
            tree_height(node.right, cur_height + 1)
        
        # checks if a node is balanced
        def balanced(node):
            self.height = 0
            tree_height(node.left, 0)
            l_height, self.height = self.height, 0
            tree_height(node.right, 0)
            r_height = self.height
            return abs(l_height - r_height) <= 1
        
        # checks if each node is balanced
        def topDownDFS(node):
            if not node: return
            # result becomes false if any one node is not balanced
            self.res = self.res and balanced(node)
            topDownDFS(node.left)
            topDownDFS(node.right)
        
        topDownDFS(root)
        return self.res """
            
        
        # optimised bottom up dfs (time = O(n))
        def bottomUpDFS(node):
            if not node: return (0, True)
            l_height, l_balanced = bottomUpDFS(node.left)
            r_height, r_balanced = bottomUpDFS(node.right)
            balanced = l_balanced and r_balanced and (abs(l_height - r_height) <= 1)
            height = max(l_height, r_height) + 1
            return (height, balanced)
        
        return bottomUpDFS(root)[1]
        
# @lc code=end


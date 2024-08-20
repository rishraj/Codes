#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
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
        # find paths of p and q and return the last common node in their paths (intuitive soln)
        """ def dfs(root, node, path):
            if not root: return
            path.append(root)
            if root.val == node.val:
                paths.append(path[:]) # imp to copy the list using slicing
                return
            dfs(root.left, node, path)
            dfs(root.right, node, path)
            path.pop() # backtracking (list is mutable, so you need to pop)
            
        paths = [] # to store paths of p and q
        dfs(root, p, [])
        dfs(root, q, [])
        path_p, path_q = paths[0], paths[1]
        # now find the index till which they are the same
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i].val != path_q[i].val:
                return path_p[i-1]
        return path_p[-1] if len(path_p) < len(path_q) else path_q[-1] """
        
        # a bit more elegant solution
        if not root or root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r: # meaning p and q are in different subtrees
            return root
        return l or r # meaning they are in same subtree and l or r store the parent among p and q

# @lc code=end


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
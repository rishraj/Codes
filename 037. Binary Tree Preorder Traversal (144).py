def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # revursive soln.
    """ res = [] # since list is mutable, self.res initialisation not needed
    def helper(node):
        if not node: return
        res.append(node.val)
        helper(node.left)
        helper(node.right)
    helper(root)
    return res """
    
    # iterative soln.
    if not root: return root # edge case
    res, stack = [], [root]
    while stack: # here root will never be null (thus, "while root or stack:" not needed)
        cur = stack.pop()
        res.append(cur.val)
        if cur.right: stack.append(cur.right) # right added before left so that it's popped later
        if cur.left: stack.append(cur.left)
    return res
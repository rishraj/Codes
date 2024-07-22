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
        node = stack.pop()
        res.append(node.val)
        if node.right: stack.append(node.right) # right added before left so that it's popped later
        if node.left: stack.append(node.left)
    return res
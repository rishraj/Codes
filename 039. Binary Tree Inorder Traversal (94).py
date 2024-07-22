def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # recursive soln.
    """ res = [] # list is mutable, hence self.res not needed
    def helper(node):
        if not node: return
        helper(node.left)
        res.append(node.val)
        helper(node.right)
    helper(root)
    return res """
    
    # iterative soln.
    # add all left childs to stack, pop last one, add to result and then change node to its right child
    res, stack = [], []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res
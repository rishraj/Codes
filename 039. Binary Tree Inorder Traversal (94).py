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
    res, stack, cur = [], [], root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res
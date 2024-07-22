def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = [] # since list is mutable, self.res initialisation not needed
    def helper(node):
        if not node: return
        res.append(node.val)
        helper(node.left)
        helper(node.right)
    helper(root)
    return res
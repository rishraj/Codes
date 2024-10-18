#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """ # storing null nodes with preorder traversal makes it uniquely identifiable
        # one can't build back a tree from preorder + inorder if the nodes aren't unique
        res = []
        def dfs(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(res) """
        
        # intuitive approach using bfs (storing null nodes as well)
        res = []
        q = deque()
        q.append(root)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    res.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
                else: res.append('N')
        return ','.join(res)
        

    def deserialize(self, data):
        """ # run dfs and dfs would return the root of the tree
        # note - data is of the form -> root leftChild leftChild leftChild ... rightChild ...
        data = data.split(',')
        self.i = 0 # would go through the entire 'data' list
        def dfs():
            if data[self.i] == 'N':
                self.i += 1
                return None
            root = TreeNode(int(data[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs() # works since 'i' has been updated to index of right child by running dfs once
            return root
        
        return dfs() """
        
        # deserialise for the bfs approach
        # keep a variable 'i' to look for children of a node
        if data[0] == 'N': return None # edge case of an empty tree
        data = data.split(',')
        root = TreeNode(int(data[0]))
        q = deque()
        q.append(root)
        i = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if data[i] != 'N':
                    node.left = TreeNode(int(data[i]))
                    q.append(node.left)
                if data[i + 1] != 'N':
                    node.right = TreeNode(int(data[i + 1]))
                    q.append(node.right)
                i += 2
        return root
                
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end


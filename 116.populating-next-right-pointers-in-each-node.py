#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        # basic soln using bfs (space = O(n))
        """ if not root: return root
        q = deque()
        q.append(root)
        while q:
            len_q = len(q)
            prev = q.popleft()
            if prev.left:
                q.append(prev.left)
                q.append(prev.right)
            for _ in range(1, len_q):
                cur = q.popleft()
                prev.next = cur
                prev = cur
                if cur.left:
                    q.append(cur.left)
                    q.append(cur.right)
        return root """
        
        # optimised soln (space = O(1))
        # traverse using two pointers (make use of next pointer)
        cur, next_level = root, root.left if root else None
        while cur and next_level:
            # process the current level
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            # process the next level when current level is over
            else:
                cur = next_level
                next_level = cur.left
        return root
        
                    
            
# @lc code=end


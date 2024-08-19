#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # next attempt -> implement using a STACK
    
        # edge case (so that helper function node is never None)
        if not head: return head

        # takes a node and returns head and tail nodes
        def helper(node):
            # if child doesn't exist recurse for the next node if it exists
            if not node.child:
                return [node, node] if not node.next else [node, helper(node.next)[1]]
            # if child exists, repair the connections and return head and tail
            else:
                res = helper(node.child)
                tmp = node.next
                node.next = res[0]
                res[0].prev = node
                node.child = None
                if tmp: # if original next node existed
                    res[1].next = tmp
                    tmp.prev = res[1]
                    return [node, helper(tmp)[1]]
                return [node, res[1]] # if original next node didn't existed
        
        return helper(head)[0] # helper function call
    
# @lc code=end


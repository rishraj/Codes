#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle of the list, split the list in 2 while reversing the 2nd half,
        # then merge by taking 1 element from each list
        
        # finding middle using slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # spliting in 2 lists while reversing second
        prev = None
        cur = slow.next
        slow.next = None # very imp. to end list 1 (otherwise cycles may appear in result)
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        # merge the 2 linked lists
        first, second = head, prev
        while second: # since 2nd list is always going to be smaller
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
# @lc code=end


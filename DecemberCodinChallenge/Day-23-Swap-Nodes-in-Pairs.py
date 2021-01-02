# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = head
        new_head = q = head.next
        prev = None
        while p and q:
            if prev:
                prev.next = q
            p.next = q.next
            q.next = p
            
            prev = p
            p = p.next
            if not p:
                break
            q = p.next
        return new_head
        

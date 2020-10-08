# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return 
        tail = head
        length = 1
        while tail.next:
            length += 1
            tail = tail.next
        newPosTail = length - (k % length) 
        if newPosTail == length:
            return head
        newTail = head
        while newPosTail != 1:
            newTail  = newTail.next
            newPosTail -= 1
        newHead = newTail.next
        newTail.next = None
        tail.next = head
        return newHead

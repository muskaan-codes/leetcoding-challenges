# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = ListNode()
        curr = l
        l.next = head
        val = 0
        while head:
            val = head.val
            while head is not None and val == head.val:
                head = head.next
            if l.next.next == head:
                l = l.next
            else:
                l.next = head
        return curr.next

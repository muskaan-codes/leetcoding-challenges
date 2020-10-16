# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        l = []
        node = head
        if not node:
            return
        while node:
            l.append(node)
            node = node.next
        l.sort(key=lambda x: x.val)
        ret = l[0]
        for x in range(len(l)-1):
            l[x].next = l[x+1]
        l[-1].next = None
        return ret

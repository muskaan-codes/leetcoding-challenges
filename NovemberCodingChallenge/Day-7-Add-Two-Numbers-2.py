# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def getVal(ln):
            s = ""
            while ln:
                s += str(ln.val)
                ln = ln.next
            return int(s)
        
        addition = getVal(l1) + getVal(l2)
        print(addition)
        self.head = ListNode(str(addition)[0])
        print(str(addition)[1:])
        for x in str(addition)[1:]:
            new_node = ListNode(x) 
            last = self.head 
            while (last.next): 
                last = last.next
            last.next =  new_node
        return self.head

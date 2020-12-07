"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root != None:
            q=deque()
            q.append(root)
            while q:
                size=len(q)
                prev=None
                while size>0:
                    curr=q.popleft()
                    curr.next=prev
                    prev=curr
                    if curr.right:
                        q.append(curr.right)
                    if curr.left:
                        q.append(curr.left)
                    size-=1
        return root

        

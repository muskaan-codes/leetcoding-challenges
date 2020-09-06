# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """

        def inOTraversal(root):
            return (inOTraversal(root.left) + [root.val] + inOTraversal(root.right)) if root else []

        l1 = inOTraversal(root1)
        l1.extend(inOTraversal(root2))
        l1.sort()
        return l1

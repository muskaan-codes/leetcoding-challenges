# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.sum = 0
        def sumBST(root, low, high):
            if root.val >= low and root.val <=high:
                self.sum += root.val
            if root.left:
                sumBST(root.left, low, high)
            if root.right:
                sumBST(root.right, low, high)
        sumBST(root, low, high)
        return self.sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def matchHeight(root):
            if not root or not self.isBalanced:
                return 0
            left = matchHeight(root.left)
            right = matchHeight(root.right)
            if abs(left-right)>1:
                self.isBalanced = False
            return max(left,right)+1
        self.isBalanced = True
        matchHeight(root)
        return self.isBalanced
        

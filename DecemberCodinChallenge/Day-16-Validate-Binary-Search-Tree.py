# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def traverse(root, mini, maxi):
            if root is None:
                return True
            if root.val <= mini or root.val >= maxi:
                return False
            if traverse(root.left, mini, root.val) and traverse(root.right, root.val, maxi):
                return True
            return False
            
        if root is None:
            return True
        return traverse(root, (-2)**31 -1, (2**31))
        
        

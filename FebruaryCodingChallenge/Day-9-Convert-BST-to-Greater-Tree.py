# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
    
        def greaterTree(node):
            if node is None:
                return
            greaterTree(node.right)
            self.sum += node.val
            node.val = self.sum
            greaterTree(node.left)
        
        greaterTree(root)
        return root
    

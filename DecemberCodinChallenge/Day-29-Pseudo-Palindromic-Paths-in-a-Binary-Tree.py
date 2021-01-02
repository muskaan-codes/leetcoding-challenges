# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node,path):
            if not node:
                return
            path ^= (1 << node.val) # tracks a count of each number
            if not node.left and not node.right:
                if path & (path - 1) == 0: # checking if it's a plandromic path
                    self.count += 1
                return
            traverse(node.left, path)
            traverse(node.right, path)    
        self.count = 0
        traverse(root,0)
        return self.count

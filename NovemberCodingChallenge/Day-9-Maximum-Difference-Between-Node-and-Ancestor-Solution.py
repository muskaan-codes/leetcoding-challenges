# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        def dfs(root, mini, maxi):
            self.result = max(abs(root.val - mini), self.result)
            self.result = max(abs(root.val - maxi), self.result)
            if root.left:
                dfs(root.left, min(root.val, mini), max(root.val, maxi))
            if root.right:
                dfs(root.right, min(root.val, mini), max(root.val, maxi))
            return self.result
        return dfs(root, root.val, root.val)

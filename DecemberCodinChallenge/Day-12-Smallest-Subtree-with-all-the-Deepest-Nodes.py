# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def getDepthAndTargetSubtree(root):
            if not root:
                return (0, None)
            leftDepth, leftTargetSubtree = getDepthAndTargetSubtree(root.left)
            rightDepth, rightTargetSubtree = getDepthAndTargetSubtree(root.right)
            if leftDepth == rightDepth:
                return (1+leftDepth, root)
            elif leftDepth < rightDepth:
                return (1+rightDepth, rightTargetSubtree)
            else:
                return (1+leftDepth, leftTargetSubtree)
        return getDepthAndTargetSubtree(root)[1]

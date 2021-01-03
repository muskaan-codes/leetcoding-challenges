# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        originalQueue = [original]
        clonedQueue = [cloned]
        while originalQueue:
            queueLength = len(originalQueue)
            while queueLength:
                nodeOriginal = originalQueue.pop()
                nodeCloned = clonedQueue.pop()
                if nodeOriginal == target:
                    return nodeCloned
                if nodeOriginal.left:
                    originalQueue.append(nodeOriginal.left)
                    clonedQueue.append(nodeCloned.left)
                if nodeOriginal.right:
                    originalQueue.append(nodeOriginal.right)
                    clonedQueue.append(nodeCloned.right)
                queueLength -= 1

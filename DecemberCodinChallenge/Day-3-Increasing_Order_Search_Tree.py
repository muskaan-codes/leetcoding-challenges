# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.nodes = []
        def inOrder(root):
            if root: 
                inOrder(root.left) 
                self.nodes.append(root.val)
                inOrder(root.right)
            else:
                return
        inOrder(root)
        i = 0
        print(self.nodes)
        output = TreeNode()
        n = output
        for i in range(0, len(self.nodes)):
            n.right = TreeNode(self.nodes[i])
            n = n.right    
        return output.right

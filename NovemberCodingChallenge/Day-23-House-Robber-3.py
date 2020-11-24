# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        max_child_sum = {}

        def dfs(node):

            if not node:
                return 0

            if node in max_child_sum:
                return max_child_sum[node]

            sub_total = 0

            if node.left:
                sub_total += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                sub_total += dfs(node.right.left) + dfs(node.right.right)

            max_child_sum[node] = max(node.val + sub_total, dfs(node.left) + dfs(node.right))

            return max_child_sum[node]

        return dfs(root)

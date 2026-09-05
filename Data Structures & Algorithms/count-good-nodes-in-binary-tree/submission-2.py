# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, maxSofar):
            nonlocal res
            if not node:
                return 
            if node.val >= maxSofar:
                res += 1
            maxSofar = max(node.val, maxSofar)
            dfs(node.left, maxSofar)
            dfs(node.right, maxSofar)
        dfs(root, float("-inf"))
        return res
        
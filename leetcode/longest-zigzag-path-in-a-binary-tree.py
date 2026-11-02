# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        bestPath = 0
        def dfs(node, direction, length):
            nonlocal bestPath 
            if not node:
                return
            bestPath = max(length, bestPath)
            if direction == "L":
                dfs(node.left, "L", 1)
                dfs(node.right, "R", length +1)
            else:
                dfs(node.left, "L", length +1)
                dfs(node.right, "R", 1)
        dfs(root, "L", 0)
        dfs(root, "R",0)
        return bestPath
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #track max in path
        good = 0
        def dfs(node, maxP):
            nonlocal good
            if not node:
                return
            if node.val >= maxP:
                good+=1
                maxP = node.val
            dfs(node.left, maxP)
            dfs(node.right, maxP)
        dfs(root, root.val)
        return good
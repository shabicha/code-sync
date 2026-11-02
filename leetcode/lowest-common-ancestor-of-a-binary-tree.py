# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        LCA = None
        def dfs(node):
            nonlocal LCA
            if not node:
                return 0
            found = 0
            if node == p or node == q:
                found = 1
            found += dfs(node.left)
            found += dfs(node.right)
            if found == 2 and LCA == None:
                LCA = node 
            return found
        dfs(root)
        return LCA
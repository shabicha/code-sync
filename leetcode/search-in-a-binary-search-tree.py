# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        rootN = None 
        def dfs(node):
            nonlocal rootN
            if not node:
                return
            
            if val == node.val:
                rootN = node
            elif val < node.val:
                dfs(node.left)
            else:
                dfs(node.right)
            return 
        
        dfs(root)
        return rootN
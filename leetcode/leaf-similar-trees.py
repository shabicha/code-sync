# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def valueS(node):
            value = []
            def dfs(node):
                if not node:
                    return 
                if not node.left and not node.right:
                    value.append(node.val)
                dfs(node.left)
                dfs(node.right)
            dfs(node)
            return tuple(value)
        
        if valueS(root1) == valueS(root2):
            return True
        return False
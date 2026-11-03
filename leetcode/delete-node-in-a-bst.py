# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        #if right, swap the del node w/ right 
        #if just left, swap 
        if not root:
            return None
     
        def dfs(node, key):
            if not node:
                return
            if node.val == key:
                if not node.right:
                    return node.left
                if not node.left:
                    return node.right
                
                succ = node.right
                while succ.left:
                    succ = succ.left
                #replace node value with relvant replacement
                node.val = succ.val
                #remove duplicate note
                node.right = dfs(node.right, succ.val)
            elif node.val < key:
                node.right = dfs(node.right, key)
            else:
                node.left = dfs(node.left, key)
            return node    
        return dfs(root, key)
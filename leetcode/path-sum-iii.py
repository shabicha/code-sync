# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        #caculate while backtracking 
        paths = 0
        path = []
        def dfs(node):
            nonlocal paths
            if not node:
                return 
            path.append(node.val)
            ssum=0
            for i in range(len(path)-1,-1,-1):
                ssum +=path[i]
                if ssum == targetSum:
                    paths+=1
            dfs(node.left)
            dfs(node.right)
            path.pop()

            
        dfs(root)
        return paths
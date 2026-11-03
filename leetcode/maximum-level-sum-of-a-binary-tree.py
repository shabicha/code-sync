# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        queue = deque([root])
        maxSum = root.val
        layer = 1
        maxLayer = 1
        while queue:
            levelSum = 0
            for i in range(len(queue)):
                node = queue.popleft()
                levelSum +=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if levelSum > maxSum:
                maxSum = levelSum
                maxLayer = layer
            layer+=1


        return maxLayer
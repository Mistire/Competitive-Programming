# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.minDepth = float('inf')
        self.dfs(root, 0)
        return self.minDepth
        
    def dfs(self, node, curDepth):
        if not node:
            return
        if not node.left and not node.right:
            self.minDepth = min(self.minDepth, curDepth + 1)
        
        self.dfs(node.left, curDepth + 1)
        self.dfs(node.right, curDepth + 1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        res = str(root.val)

        if root.left or root.right:
            left_str = self.tree2str(root.left)
            res += f'({left_str})'
        if root.right:
            right_str = self.tree2str(root.right)
            res += f'({right_str})'
        
        return res
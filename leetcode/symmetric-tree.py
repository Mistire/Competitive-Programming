# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # def dfs(left, right):
        #     if not left and not right:
        #         return True
        #     if not left or not right:
        #         return False
            
        #     return(left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left))
        
        # return dfs(root.left, root.right)
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return isSameTree(p.left, q.right) and isSameTree(p.right, q.left)

        return isSameTree(root.left, root.right) if root else True
        
        
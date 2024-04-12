# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([root])

        while q:
            level = set()
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    level.add(node.left.val)
                if node.right:
                    q.append(node.right)
                    level.add(node.right.val)
                if node.right and node.left:
                    if {node.right.val, node.left.val} == {x,y}:
                        return False
            if x in level and y in level:
                return True
            
        
                

                


            
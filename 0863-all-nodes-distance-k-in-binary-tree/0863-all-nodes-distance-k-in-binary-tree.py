# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parentMap = {}
        def dfs(node, parent=None):
            if not node:
                return
            parentMap[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root)

        vis = set()
        queue = deque([(target, 0)])
        res = []

        while queue:
            node, distance = queue.popleft()

            if node in vis:
                continue
            vis.add(node)
            # print(vis)
            if distance == k:
                res.append(node.val)
            elif distance < k:
                for nei in (node.left, node.right, parentMap[node]):
                    if nei and nei not in vis:
                        queue.append((nei, distance+1))
        
        return res


        
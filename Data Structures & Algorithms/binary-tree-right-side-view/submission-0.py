# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Binary Tree
DFS down the right side

res = []

dfs(node, depth):
    if node is null
        return
    
    if depth == length(res)
        res.append(node.val)

    dfs(right, depth + 1)
    dfs(left, depth + 1)

dfs(root, 0)



"""

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, depth):
            if not node:
                return 

            if depth == len(result):
                result.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)

        return result


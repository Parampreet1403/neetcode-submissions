# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # Recursion
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        return max(leftDepth, rightDepth) + 1

"""
BFS and count Level

OR DFS and keep the max

DFS
if node is None:
    return 0;

Recursion
leftDepth = maxDepth(root.left)
rightDepth = maxDepth(root.right)

return max(leftDepth, rightDepth) = 1

"""
        
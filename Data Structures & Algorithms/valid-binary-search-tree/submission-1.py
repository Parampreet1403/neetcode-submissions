# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
8:42
Binary Tree -> each node has 2 children
Is this a valid BST
BST 


DFS + limit
* left children inherent an upper bound 
* right children inherent a lower bound

Q -> am i < upper bound and i > lower bound
as long as this is true for every node we have a BST

dfs(node, ll, ul):
    if not node
        return True
    
    if node.val >= ul or node.val <= ll:
        return false

    leftbst = dfs(node.left, ll, node.val)
    rightbst = dfs(node.right, node.val, ul)

    return leftBst and rightBst

dfs(node, -inf, +inf)

# Edge cases
empty -> return true
sindle node -> return true

"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True

            if node.val >= high or node.val <= low:
                return False
            
            leftBst = dfs(node.left, low, node.val)
            rightBst = dfs(node.right, node.val, high)

            return leftBst and rightBst

        return dfs(root, -1001, 1001)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Binary Tree
BFS, DFS
DFS

good -> from root to x contains no nodes with a value greater than x

*  if the node seen is greater then the root then this is a good node?

node nodeVal > runningMax
running max needs to be updated 

dfs(node, runningMax):
    if node is null
        return 0

    if node.val > runningMax:
        # good node
        count = 1
    
    newMax = max(runningMax, node.val)
    leftCount = dfs(node.left, newMax)
    rightCount = dfs(node.right, newMax)

    return leftCount + rightCount + count

dfs(root, -max_int)

edge cases
empty ->return 0
single node -> 1

"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, runningMax):
            if node is None:
                return 0

            count = 0
            if node.val >= runningMax: # can be >= ?
                count = 1
            
            newMax = max(runningMax, node.val)
            lc = dfs(node.left, newMax)
            rc = dfs(node.right, newMax)

            return lc + rc + count

        return dfs(root, -101)

        
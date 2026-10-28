# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height(node):
            if not node:
                return 0

            lh = height(node.left)
            rh = height(node.right)

            self.diameter = max(self.diameter, lh + rh)

            return 1 + max(lh, rh)

        height(root)

        return self.diameter

        

"""
Diameter - length of the path between any two nodes
Trying to get the longest Path between any two Nodes
Does not need to pass through the route 

What is the longest length between any two nodes?

Node
leftSubTree ?
rightSubTree ?

Compare these subtrees for every node 
and keep a cached max for every node

DFS

int diamete = 0

int height(node) {
    if node is null
        return 0

    left_h = height(node.left)
    right_h = height(node.right)
    diamete = max(best, left_h + right_h)

    return 1 + max(left_h, right_h)
}

height(node)
return diameter

"""


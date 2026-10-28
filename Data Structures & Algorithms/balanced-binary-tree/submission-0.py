# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Binary Tree

return true if balanced

balanced -> left and right subtrees of every node differe in height by no more than 1

So each node needs to ask its children are you balanced
If even one child is not balanced then we can assume the whole tree is not balanced

Bottom Up -> DFS -> Recursion -> PostOrder

void check (node) {
    if node == nullptr
        return true, 0
    
    leftB, lh = check(node.left)
    if not leftB:
        return false, 0

    rightB, rh = check(node.right)
    if not rightB:
        return false, 0

    abs(lh - rh) > 1:
        return false

    return true, 1 + max(lh, rh)
}


"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfsCheck(node):
            if not node:
                return True, 0
            
            leftB, lh = dfsCheck(node.left)
            if not leftB:
                return False, 0

            rightB, rh = dfsCheck(node.right)
            if not rightB:
                return False, 0

            if abs(lh - rh) > 1:
                return False, 0

            return True, 1 + max(lh, rh)
        
        ans, h = dfsCheck(root)
        return ans
            


            



        
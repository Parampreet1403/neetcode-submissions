# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
BST -> 2 node children 
Left subtree smaller 
Right Subtree greater

int k

DFS, BFS

BFS
LNR

stack
curr = root

while stack is not empty while curr is not none
    while curr is not none
        stack.append(curr)
        curr = curr.left

    node = stack.pop()
    k--

    if k == 0:
        return node.val

    curr = curr.right



"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            node = stack.pop()
            k = k-1
            if k == 0:
                return node.val

            curr = node.right

        return 0
        
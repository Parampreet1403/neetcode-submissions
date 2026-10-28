# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Binary Tree
Level Order Traversal
Queue
BFS

q = queue()
q.push(root)
result = [[]]

while q is not empty():
    level_size = q.size()
    level = []
    for i in level_sizw:
        node = q.pop()
        level.append(q.val)
        if node.left
            q.push_back(node.left)
        if node.right
            q.push_back(node.right)
    append level to result

return result

Edge cases:
    empty return emptry
    single node returns single node


"""

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level_len = len(q)
            level = []

            for i in range(level_len):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(level)

        return res


        
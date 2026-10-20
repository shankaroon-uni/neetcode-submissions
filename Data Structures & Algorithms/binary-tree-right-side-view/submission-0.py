# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()
        queue.append([root])
        res = []

        while queue:
            level = queue.popleft()
            temp = []
            children = []
            if level:
                for node in level:
                    if node:
                        temp.append(node)
                        children.append(node.left)
                        children.append(node.right)
                queue.append(children)
                if temp:
                    res.append(temp[-1].val)
        return res
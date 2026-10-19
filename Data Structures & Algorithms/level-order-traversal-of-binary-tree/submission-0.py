# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append([root])
        res = []

        while queue:
            node = queue.popleft()
            if node:
                temp = []
                childTemps = []
                for n in node:
                    if n:
                        temp.append(n.val)
                        if n.left:
                            childTemps.append(n.left)
                        if n.right:
                            childTemps.append(n.right)
                if temp:
                    res.append(temp)
                
                queue.append(childTemps)
                
               
        return res
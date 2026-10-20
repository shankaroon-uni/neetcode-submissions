# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 1
        def check(prev, root):
            nonlocal res
            if root is None:
                return None
            if prev and prev <= root.val:
                res += 1
            if not prev:
                temp = root.val
            else:
                temp = max(prev, root.val)
            check(temp, root.left)
            check(temp, root.right)
            return res
        
        return check(None, root)

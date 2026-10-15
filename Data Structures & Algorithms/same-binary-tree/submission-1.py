# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pstack = [(p, False)]
        qstack = [(q, False)]

        while pstack and qstack:
            pnode, pcheck = pstack.pop()
            qnode, qcheck = qstack.pop()
            if pnode and qnode:
                if pcheck and qcheck:
                    if pnode.val != qnode.val:
                        return False
                else:
                    pstack.append((pnode.left, False))
                    qstack.append((qnode.left, False))
                    pstack.append((pnode.right, False))
                    qstack.append((qnode.right, False))
                    pstack.append((pnode, True))
                    qstack.append((qnode, True))
            elif pnode or qnode:
                return False

        return True
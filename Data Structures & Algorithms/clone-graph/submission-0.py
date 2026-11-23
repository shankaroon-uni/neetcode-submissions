"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned = {}

        def dfs(real):
            if real in cloned:
                return cloned[real]

            copy = Node(real.val)
            cloned[real] = copy

            for n in real.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        return dfs(node)
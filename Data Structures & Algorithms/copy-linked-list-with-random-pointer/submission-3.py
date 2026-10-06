"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapped = {}
        first = head

        while first:
            mapped[first] = Node(first.val)
            first = first.next

        for node in mapped:
            if node.next != None: 
                mapped[node].next = mapped[node.next]
            if node.random != None:
                mapped[node].random = mapped[node.random]
        if mapped:
            return mapped[head]

        return first
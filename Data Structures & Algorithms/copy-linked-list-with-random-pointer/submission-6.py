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
        mapped = {None:None}
        first = head

        while first:
            mapped[first] = Node(first.val)
            first = first.next

        cur = head
        while cur:
            mapped[cur].next = mapped[cur.next]
            mapped[cur].random = mapped[cur.random]
            cur = cur.next

        return mapped[head]


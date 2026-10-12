# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fullLength = 0
        start = head
        while start:
            fullLength += 1
            start = start.next

        remove = fullLength - n
        if remove == 0:
            return head.next

        cur = head
        for i in range(fullLength - 1):
            if (i + 1) == remove:
                cur.next = cur.next.next
                
            cur = cur.next
        return head
        

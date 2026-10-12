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

        s = 0
        remove = fullLength - n
        if remove == 0:
            return head.next
        new = head
        last = head
        while s != remove:
            s +=1
            last = new
            new = new.next

        new = new.next

        last.next = new

        return head
        

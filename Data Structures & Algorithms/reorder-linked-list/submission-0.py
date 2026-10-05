# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        midpoint = slow.next
        slow.next = None

        prev = None
        while midpoint:
            nxt = midpoint.next
            midpoint.next = prev
            prev = midpoint
            midpoint = nxt
        
        r = head
        l = prev

        while r and l:
            tmpR = r.next
            r.next = l
            tmpL = l.next
            r = r.next
            r.next = tmpR

            r = tmpR
            l = tmpL

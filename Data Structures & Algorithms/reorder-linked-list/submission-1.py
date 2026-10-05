# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        one = head
        two = prev

        while one and two:
            nxtOne = one.next
            nxtTwo = two.next

            one.next = two
            two.next = nxtOne

            one = nxtOne
            two = nxtTwo
        
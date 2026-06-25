# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)

        dummy.next = head

        prev = dummy
        first = dummy.next

        while first and first.next:
            second = first.next
            next1 = second.next

            #swap
            prev.next = second
            first.next = next1
            second.next = first

            #reset
            prev=first
            first = first.next
        return dummy.next
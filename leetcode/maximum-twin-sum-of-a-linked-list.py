# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        slow = head
        fast = head
        while fast:
            slow = slow.next
            fast = fast.next.next
        
        p1 = slow
        p2 = slow.next
        p1.next = None

        while p2:
            next1 = p2.next
            p2.next = p1

            p1 = p2
            p2 = next1

        tail = p1
        maxT = 0

        while tail:
            maxT = max(tail.val + head.val, maxT)
            tail = tail.next
            head = head.next
        return maxT
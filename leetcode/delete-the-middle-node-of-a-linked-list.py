# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        # fast & slow pointer to find middle - slow = middle 
        slow = head
        fast = head
        slowP = head
        if not fast.next:
            return None
        if fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            slowP=slowP.next
        
        slowP.next = slow.next
        return head
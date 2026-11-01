# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        
        p1 = head
        p2 = head.next
        p1.next = None
        
        while p1 and p2:
            next1 = p2.next
            p2.next = p1
            #update
            p1 = p2
            p2=next1
        return p1
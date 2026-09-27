# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        
        cur = head
        prev= None
        while cur:
            #save next element 
            saved = cur.next
            #reroute cur -> prev
            cur.next = prev

            #reset values
            prev=cur
            cur = saved
            
            
        return prev
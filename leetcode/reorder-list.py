# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #fast & slow
        fast = slow = head
        while fast.next and fast.next.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        s=slow.next
        slow.next =None

        #reverse 2nd half
        prev = None
        cur = s
        
        while cur:
            next1=cur.next
            cur.next = prev
            prev = cur
            cur = next1
        
        pointer2=prev
        # alternatingly to first list until end reached
        pointer1 = start = head
        while pointer1 and pointer2:
            next1 = pointer1.next
            next2 = pointer2.next

            pointer1.next = pointer2
            pointer2.next = next1

            pointer1 = next1
            pointer2=next2
        
        if pointer2:
            pointer1.next = pointer2
        

        return start
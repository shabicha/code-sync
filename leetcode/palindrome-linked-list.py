# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        #fast and slow
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse slow
        prev = None
        cur = slow
        while cur:
            next1 = cur.next
            cur.next = prev

            prev = cur
            cur = next1
        
        #check p1 and prev, if not equal return false else true
        p1=head
        while prev:
            if p1.val != prev.val:
                return False
            p1 = p1.next
            prev = prev.next

        return True
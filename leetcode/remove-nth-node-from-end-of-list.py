# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        p2 = head
        u=0
        while p2:
            u +=1
            p2 = p2.next

        
        x=ListNode(0)
        x.next = head
        prev=x
        p1 = head
        count =0
        while p1:
            if count == u-n:
                prev.next = p1.next
            prev = p1
            p1 = p1.next
            
            count +=1
        
        return x.next
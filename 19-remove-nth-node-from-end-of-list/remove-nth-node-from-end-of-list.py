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
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        index_to_remove = count - n  
        dummy = ListNode(0, head)
        curr = dummy
        
        for _ in range(index_to_remove):
            curr = curr.next
        curr.next = curr.next.next
        
        return dummy.next       
        
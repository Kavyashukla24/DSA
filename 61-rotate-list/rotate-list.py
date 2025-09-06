# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if k == 0 or head is None:
            return head
        curr = head
        length = 1  
        while curr.next is not None:
            curr = curr.next
            length += 1
        curr.next = head
        k %= length
        if k == 0:
            curr.next = None  
            return head
        temp = head
        for _ in range(length - k - 1):
            temp = temp.next
        new_head = temp.next
        temp.next = None  

        return new_head

        
        
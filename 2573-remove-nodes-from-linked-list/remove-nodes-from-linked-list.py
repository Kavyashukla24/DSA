# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        head = reverse(head)
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head
        max_so_far = float('-inf')

        while curr:
            if curr.val >= max_so_far:
                max_so_far = curr.val
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next
        return reverse(dummy.next)
            

        
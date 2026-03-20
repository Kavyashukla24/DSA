# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1, p2= headA, headB
        l1, l2=0,0
        while(p1!=None):
            l1+=1
            p1=p1.next
        while(p2!=None):
            l2+=1
            p2=p2.next
        
        p1,p2=headA,headB
        extra= max(l1,l2)- min(l1,l2)
        if(l1>l2):
            for i in range(extra):
                p1=p1.next
        else:
            for i in range(extra):
                p2=p2.next
        
        while(p1!=p2 and p1!=None and p2!=None):
            p1=p1.next
            p2=p2.next
        
        if(p1!=None and p2!=None):
            return(p1)
        else:
            return(None)
        

        
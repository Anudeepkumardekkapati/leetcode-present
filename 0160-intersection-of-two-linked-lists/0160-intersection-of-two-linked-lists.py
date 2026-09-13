# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:

        len1=0
        len2=0

        a=head1
        b=head2

        while a:
            a=a.next
            len1+=1
        while b:
            b=b.next
            len2+=1
        
        a=head1
        b=head2
        
        while len1>len2:
            a=a.next
            len1-=1
        
        while len2>len1:
            b=b.next
            len2-=1
        

        while a!=b:
            a=a.next
            b=b.next
        
        return b
        

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        curr=head
        l=0

        while curr:
            l+=1
            curr=curr.next
        
        lens=l//2

        curr=head
        i=1
        while i!=lens:
            curr=curr.next
            i+=1
        
        return curr.next

        
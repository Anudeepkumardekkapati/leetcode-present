# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=0
        curr=head

        while curr:
            l+=1
            curr=curr.next
        
        ans=l//2

        for i in range(ans):
            head=head.next
        
        return head
        
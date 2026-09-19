# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        l=0
        curr=head
        while curr:
            l+=1
            curr=curr.next
        

        curr=head
        l1=l//2
        if l1<1:
            return head
        
        num=0
        while num<l1:
            num+=1
            curr=curr.next
        return curr
        
        
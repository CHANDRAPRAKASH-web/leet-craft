# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        current=head
        l=0
        i=head
        while i is not None:
            l+=1
            i=i.next
        if l==n:
            head=current.next
            return head
        ptr=-1
        while current is not None:
            ptr+=1
            if ptr==l-n-1:
                current.next=current.next.next
            current=current.next
        return head


            
                



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        odd_ptr=head
        even_ptr=head.next
        temp=head.next
        while even_ptr and even_ptr.next:
            odd_ptr.next=odd_ptr.next.next
            even_ptr.next=even_ptr.next.next
            
            odd_ptr=odd_ptr.next
            even_ptr=even_ptr.next
        odd_ptr.next=temp
        return head

        
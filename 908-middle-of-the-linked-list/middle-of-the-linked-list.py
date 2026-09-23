# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        length=0
        current_node=head
        while current_node is not None:
            length+=1
            current_node=current_node.next
        target=length//2
        current_node=head
        for i in range(target):
            current_node=current_node.next
        head=current_node
        return head

        
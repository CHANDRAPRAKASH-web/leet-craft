class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0
        
    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        current_node=self.head
        for i in range(index+1):
            if i==index:
                return current_node.val
            current_node=current_node.next
        

        
        

    def addAtHead(self, val: int) -> None:
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
        self.size+=1
        

    def addAtTail(self, val: int) -> None:
        new_node=Node(val)
        if self.size==0:
            new_node.next=None
            self.head=new_node
        elif self.size==1:
            self.head.next=new_node
            new_node.next=None
        else:
            current_node=self.head
            while current_node.next is not None:
                current_node=current_node.next
            current_node.next=new_node
            new_node.next=None
           
        self.size+=1


    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.size:
            return
        new_node=Node(val)
        if index==0 or self.size==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current_node=self.head
            for i in range(1,index):
                current_node=current_node.next
            new_node.next=current_node.next
            current_node.next=new_node
        self.size+=1
            
                
        

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size:
            return
        if index==0:
            self.head=self.head.next
        else:
            current_node=self.head
            for i in range(1,index):
                current_node=current_node.next
            current_node.next=current_node.next.next

        self.size-=1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
        #insrt new node at beg
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def dtct_nd_rmv(self):
        if self.head is None:#ll empty
            return
        if self.head.next is None:#ll has 1 node
            return
        slow=self.head
        fast=self.head
        while (slow and fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        #if slow and fast meet at some pt there is a loop
            if slow==fast:
                print('Meeting point',slow.data)
                slow=self.head
                #finding the begng of loop
                while (slow.next!=fast.next):
                    slow=slow.next
                    fast=fast.next
                    #since fast.next is looping pt
                print('start of loop',fast.next.data)
                fast.next=None#remove loop
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next
llist=ll()
llist.head=Node(50)
llist.head.next=Node(20)
llist.head.next.next=Node(15)
llist.head.next.next.next=Node(4)
llist.head.next.next.next.next=Node(10)
#create a loop for testing
extra=Node(1)
llist.head.next.next.next.next.next=extra
extra.next=llist.head.next
#llist.print()
llist.dtct_nd_rmv()
print('l.l after removing loop')
llist.print()

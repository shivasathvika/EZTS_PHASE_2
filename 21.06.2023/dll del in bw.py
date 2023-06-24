#create node
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete(self,pos):
        temp=self.head.next
        prev=self.head
        #2 iterations
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next#20 1 point 40
        temp.next=None
    def display(self):
        if self.head is None:
            print('empty')
        else:
            temp=self.head
            while temp:
                 if temp.next!=None:
                    print(temp.data,end=" <--> ")
                 else:
                    print(temp.data,end=" ")
            #temp.data means first node's data
                 temp=temp.next
l=dll()
n1=node(100)
l.head=n1
n2=node(200)
n2.prev=n1
n1.next=n2
n3=node(300)
n3.prev=n2
n2.next=n3
l.display()
print()
l.delete(2)
l.display()

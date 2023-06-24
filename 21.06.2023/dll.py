class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print('Empty')
        else:
            temp=self.head
            while temp:
                if temp.next!=None:
                    print(temp.data, end= '<-->')
                else:
                    print(temp.data,end=' ')
                #temp.data means first node's data
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(300)
n3.prev=n2
n2.next=n3
l.display()

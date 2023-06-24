#     CREATING NODE-DECLERATION & DEFINATION
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
        self.last_node=None
    def delete_last(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def delete_1st(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def del_pos(self,pos):
        temp=self.head.next
        prev=self.head
        #2 iterations
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next#20 1 point 40
        temp.next=None#30 next will be will
    def  display(self):
        if self.head is None:
            print('l.l is empty')
        else:
            temp=self.head #temp =first node
            while temp:
                if temp.next!=None:
                    print(temp.data, end= '->')
                else:
                    print(temp.data,end=' ')
                #temp.data means first node's data
                temp=temp.next
obj=singlelinkedlist()
#node creation - instialising
n=Node(10) #so n.data in node class will be 10
obj.head=n        #assinging 1st node as head
n1=Node(20)
obj.head.next=n1        # next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
print('before del')
obj.display()
print('\nafter del from 1st')
obj.delete_1st()
obj.display()
print('\nafter del frm last')
obj.delete_last()
obj.display()
print('\ndel from a pos')
obj.del_pos(2)
obj.display()

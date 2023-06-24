'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def delete_1st(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delete_last(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
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
obj=sll()

print('select an option')
print('1.del from 1st 2.del from end 3.del from a pos')
n=int(input())
if n>0 and n<4:
    if (n==1):
        print('after del frm 1st')
        obj=sll()
        obj.delete_1st()
    if (n==2):
        print('after del from last')
        obj.delete_last()
    if (n==3):
        print('\ndel from a pos')
        obj.del_pos(2)
        obj.display()
else:
    print('enter  valid option')'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def delete_at_begin(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            self.head=self.head.next
            print(temp.data,"is deleted successfully")
            del(temp)
        print("Delete at Begin operation is completed successfully")
    
    def delete_at_position(self,pos):
        if self.head is None:
            print("List is Empty")
        else:
            count=0
            temp=self.head
            if pos==0:
                temp=self.head
                self.head=self.head.next
                print(temp.data,"is deleted successfully")
                del(temp)
            else:
                prev=None
                while (pos)!=count and temp is not None:
                    prev=temp
                    temp=temp.next
                    count+=1
                if temp==None:
                    print("Index out of range")
                else:
                    prev.next=temp.next
                    print(temp.data,"is deleted successfully")
                    del(temp)
            print('Delete at Position operation completed successfully')
    
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            prev=None
            while temp.next:
                prev=temp
                temp=temp.next
            prev.next=None
            print(temp.data,"is deleted successfully")
            del(temp)
        print("Delete at End operation is completed successfully")

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=' ')
                if temp.next!=None:
                    print('->',end=' ')
                temp=temp.next
        print("\nDisplay operation completed successfully")
o=SLL()
n=int(input('How many elements would you like to enter'))
for i in range(n):
    data=int(input('Enter data item:'))
    o.append(data)
print('The linked list:',end=' ')
print("1.Delete at Begin\n2.Delete at Position\n3.Delete at end\n4.Search\n5.Display\n6.Exit\n")
o=SLL()
while True:
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        o.delete_at_begin()
    elif ch==2:
        pos=int(input("Enter Position to delete:"))
        o.delete_at_position(pos)
    elif ch==3:
        o.delete_at_end()
    elif ch==4:
        num=int(input("Enter Number to Search:"))
        o.search(num)
    elif ch==5:
        o.display()
    elif ch==6:
        print('\n\t*******Your Exited******\n\t\tTHE END*\n')
        break
    else:
        print("Invalid Entry\nTry Once Again")

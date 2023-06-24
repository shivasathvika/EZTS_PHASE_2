class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            new=Node(data)
            new.next=self.head
            self.head=new
    def pop(self):
        if self.head is None:
            return None
        else:
            popped=self.head.data
            self.head=self.head.next
            return popped
    def display():
        print(stack)
obj=stack()
while True:
    print('push <value>')
    print('pop')
    print('quit')
    print('display')
    do=input('What would you like to do?').split()
    print('do',do)
    print('do[0]',do[0])
    op=do[0].strip().lower()
    if op=='push':
        obj.push(int(do[1]))
    elif op=='pop':
        popped=obj.pop()
        if popped is None:
            print('Stack is empty')
        else:
            print('Popped value:',int(popped))
    elif op=='display':
        obj.display()
    elif op=='quit':
        break

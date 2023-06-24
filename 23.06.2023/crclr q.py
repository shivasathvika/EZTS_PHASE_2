class CircularQueue():
    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1
    def enqueue(self,data):
        #condtn if q is full
        if ((self.rear+1)%self.size==self.front):#size 6 index 0-5
            print('Queue is full\n')
            #cndtn if q is empty
        elif(self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
            #always add element at rear 
        else:
            #next pos of rear
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
    def dequeue(self):
        if(self.front==-1):
        #cndtn for empty q
            print('q is empty\n')
            #cndtn for only 1 element
        elif(self.front==self.rear):
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
    def display(self):
        #cndtn fot empty q
        if(self.front==-1):
            print('Q is empty')
        elif(self.rear>=self.front):
            print('Elements in the circular queue',end=' ')
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=' ')
            print()
        elif ((self.rear+1)% self.size==self.front):
           print('Q is full ')
        else:
            print('elements:',end=' ')
            for i in range(self.front,self.size):
                print(self.queue[i],end=' ')
            for i in range(0,self.rear+1):
                print(self.queue[i],end=' ')
            print()
ob=CircularQueue(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-6)
ob.display()
print('Deleted value=',ob.dequeue())
print('Deleted value=',ob.dequeue())
ob.display()
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
ob.display()
#it wont be inserted bcoz q is full
ob.enqueue(100)
ob.display()

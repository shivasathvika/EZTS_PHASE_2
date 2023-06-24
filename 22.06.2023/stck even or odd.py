s1=[]
s2=[]
def push():
    for i in range(5):
        element=int(input('Enter the element'))
        if (element%2==0):
            s1.append(element)
        else:
            s2.append(element)
def pop():
    pop_wt=input('1 or 2: ')
    if pop_wt=='1':
        if not s1:
            print('stack is empty')
        else:
            e=s1.pop()
            print('removed element:',e)
            print(s1)
    else:
        if not s2:
            print('stack is empty')
        else:
            e=s2.pop()
            print('removed element',e)
            print(s2)
def show():
    what=input('1 or 2:')
    if what=='1':
        print(s1)
    else:
        print(s2)
while True:
    print('select operation 1.push 2.pop 3.show 4.quit')
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        show()
    elif choice==4:
        break
    else:
        print('Enter a valid option')

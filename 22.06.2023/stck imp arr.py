stack=[]
def push():
    element=int(input('Enter  elemet:'))
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print('Stack is empty')
    else:
        e=stack.pop()
        print('Remove element',e)
        print(stack)
def top():
    if not stack:
        print('Stack is empty')
    else:
        e=stack.pop()
        print('top is',e)
        #print('top is',stack[-1])
def display():
    print(stack)
while True:
    print('Select operation 1.Push 2.Pop 3.Display 4.top 5.Quit')
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()
    elif choice==4:
        top()
    elif choice==5:
        break
    else:
        print('Enter a valid option')


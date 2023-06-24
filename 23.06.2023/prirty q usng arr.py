'''append elements(key,value)
key:priority
value:element in q
and sort list every time in element is appended'''
grade=[]
grade.append((1,'Akash'))
grade.append((4,'Ankitha'))
grade.sort(reverse=True)
print('Yes')
print(grade)
grade.append((3,'sid'))
grade.sort(reverse=True)
grade.append((2,'Akshay'))
grade.sort(reverse=True)
print('Priorities sorted')
print(grade)
print('Original queue')
while grade:
    print(grade.pop())


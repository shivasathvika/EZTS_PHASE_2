r=int(input("Enter no of the rows:"))
c=int(input("Enter no of the columns:"))
matrix=[]
for i in range(r):
    a=[]
    for i in range(c):
        x=int(input("Enter the item:"))
        a.append(x)
    matrix.append(a)
print("The Matrix is:")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
print("The diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i==j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Non diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i!=j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Upper diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i<j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Lower diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i>j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Transpose Matrix is:")
for i in range(r):
    for j in range(c):
        print(matrix[j][i],end=" ")
    print()
'''n=int(input("Enter row Size of the matrix:"))
m=int(input("Enter col size of the matrix:"))
if m==n:
    matrix=[]
    print("Enter the Martix below:")
    for i in range(n):
        matrix.append(list(map(int,input().split())))
    diagonal=[]
    non_diagonal=[]
    lower_diagonal=[]
    upper_diagonal=[]
    for i in range(n):
        for j in range(m):
            if i==j:
                diagonal.append(matrix[i][j])
            elif i<j:
                upper_diagonal.append(matrix[i][j])
                non_diagonal.append(matrix[i][j])
            elif i>j:
                lower_diagonal.append(matrix[i][j])
                non_diagonal.append(matrix[i][j])
    print("Diagonal Elements:\n")
    for i in range(len(diagonal)):
        print(' '*i,diagonal[i])
    print()
    print("Non Diagonal Elements:\n")
    for i in range(n):
        for j in range(m):
            if i==j:
                print(' ',end='')
            else:
                print(matrix[i][j],end=' ')
        print()
    print("Upper Diagonal Elements:")
    for i in range(n):
        for j in range(m):
            if i<j:
                print(matrix[i][j],end=' ')
            else:
                print(' ',end=' ')
        print()
    print("Lower Diagonal Elements:")
    for i in range(n):
        for j in range(m):
            if i>j:
                print(matrix[i][j],end=' ')
        print()
else:
    print("It won't work for rectangular matrix")'''

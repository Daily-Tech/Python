#function for getting input of matrix
def matrix(m,n):
    mat=[]
    for i in range(m):
        row=[]
        for j in range(n):
            val=int(input(f'Enter value of [{i}][{j}] :'))
            row.append(val)
        mat.append(row)
    return mat

#method for Add two matrix,A and B
def add(A,B):
    output=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output

#method for Subtrac two matrix, B from A
def sub(A,B):
    output=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        output.append(row)
    return output

#method for Multiply two matrix, A and B
def mul(A,B):
    output=[]
    for i in range(len[A]):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j] * B[i][j])
        output.append(row)
    return output

#method for Divide two matrix, A by B
def div(A,B):
    output=[]
    for i in range(len[A]):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j] / B[i][j])
        output.append(row)
    return output

#method to display matrix in formate
def display(A):
        for i in range(len(A)):
            for j in range(len(A[0])):
                print(A[i][j],end=" ")
            print()

#taking input row and column from user m,n               
m=int(input('Enter the row :'))
n=int(input('Enter the column :'))

print('Enter matrix A')
A=matrix(m,n)
print(display(A))

print('Enter matrix B')
B=matrix(m,n)
print(display(B))

print('Display Addition of two matrix, A and B :')
a=add(A,B)
print(display(a))

print('Display Subtraction of two matrix, B from A :')
s=sub(A,B)
print(display(s))

print('Display Multiplication of two matrix, A and B :')
m=mul(A,B)
print(display(m))

print('Display Division of two matrix, A by B :')
d=div(A,B)
print(display(d))

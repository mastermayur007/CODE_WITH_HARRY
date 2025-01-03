def matrix(m,n):
    o=[]
    for i in range(m):
        row=[]
        for j in range(n):
            inp=int(input(f"enter o[{i}][{j}]:\n"))
            row.append(inp)
        o.append(row)
    return o

def sum(A,B):
    output=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j]+B[i][j])
        output.append(row)
    return output
                

m=int(input("enter the value of m:\n"))
n=int(input("enter the value of n:\n"))
print("enter the elements of matrix A:")
A=matrix(m,n)
print(A)

print("enter the elements of matrix B:")
B=matrix(m,n)
print(B)

s=sum(A,B)
print(s)
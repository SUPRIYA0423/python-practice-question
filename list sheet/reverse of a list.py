#reverse of a list using for loop
A=list(map(int,input("enter the numbers:").split()))
reversed=[]
for i in range(len(A)-1, -1, -1):
    reversed.append(A[i])
print(reversed)
#square of list
A=list(map(int,input("enter the number:").split()))
B=[]
for num in A:
    B.append(num*num)
print(B)
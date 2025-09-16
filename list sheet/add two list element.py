#add two list element 
a=list(map(int,input("enter the first list:").split()))
b=list(map(int,input("enter the second list:").split()))
c=[]
for i in range(len(a)):
    c.append(a[i] + b[i])    
print(c)
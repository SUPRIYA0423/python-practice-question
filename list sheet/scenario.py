n=int(input())
c=list(map(int,input().split()))
even=[]
for i in c:
    if i % 2 == 0:
        even.append(i)
if c:
    print(c)
else:
    print(-1)           
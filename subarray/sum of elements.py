n=int(input())
arr=list(map(int,input().split()))
L,R=map(int,input().split())
L-= 1
R-= 1
sum=0
for i in range(L,R+1):
    sum+=arr[i]
print(sum)
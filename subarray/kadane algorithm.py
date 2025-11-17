n=int(input())
a=list(map(int,input().split()))
max=a[0]
sum=0
for x in a:
    sum += x
    if sum > max:
        max=sum
    if sum < 0:
        sum = 0
print(max)
#first occurence
a=input()
b=int(input())
f=-1
for i in range(len(a)):
    if ord(a[i]) == b:
        f=i
        break
print(f)
#separate even and odd
a=list(map(int,input("enter the number:").split()))
for num in a:
    if num % 2 == 0:
        print(num,end="")
print()
for num in a:
    if num % 2 != 0:
        print(num,end="")
print()        
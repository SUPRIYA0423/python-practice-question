#three integers and their maximum
a=int(input("enter the first number:"))
b=int(input("enter the first number:"))
c=int(input("enter the first number:"))
if a>b and a>c:
    print("a is the maximum number")
elif b >= a and b >= c:
    print("b is the maximum number")
else:
    print("c is the maximum number")
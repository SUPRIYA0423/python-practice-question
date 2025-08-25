#printing minimum element 
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if a<=b and a<=c:
    minimum=a
elif b<=a and b<=c:
    minimum=b
else:
    minimum=c
print("minimum is:",minimum)
#5 A is divisible by both 5 and 11 or not.
A=int(input("enter the number:"))
if A % 5==0 and A % 11 == 0:
    print("A is divisible by both number ")
else:
    print("A is not divisible by both number")
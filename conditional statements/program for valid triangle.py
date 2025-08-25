A=int(input("enter the first angle:"))
B=int(input("enter the seocnd angle:"))
C=int(input("enter the third angle:"))
if A+B+C==180 and A>0 and B>0 and C>0:
    print("triangle is valid")
else:
    print("invalid")
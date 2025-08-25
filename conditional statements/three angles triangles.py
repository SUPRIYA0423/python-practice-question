#three angles of triangle and their types
C=int(input("enter the first angle:"))    
D=int(input("enter the second angle:"))
E=int(input("enter the third angle:"))
if C == 90 or D == 90 or E == 90:
    print("it is a right angle triangle")
elif C >=90 or D >= 90 or E >= 90: 
    print("it is an obtuse triangle")
else:
    print("it is an acute triangle")
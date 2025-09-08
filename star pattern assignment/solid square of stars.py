#solid square of stars
n = int(input("Enter row: "))
m= int(input("enter column:"))
for i in range(0,n):
    for j in range(0,m):
        print(" * ", end="")
    print()
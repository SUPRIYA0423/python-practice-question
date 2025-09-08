#off star pattern
# take number of rows from user
n = int(input("Enter number of rows: "))
for i in range(n):
    if i == n // 2:     
        print("*")
    else:               
        print("* *")

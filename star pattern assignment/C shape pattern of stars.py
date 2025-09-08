# C shape pattern of stars
# take user input
a = int(input("Enter rows: "))
b = int(input("Enter column: "))

for i in range(a):
    if i == 0 or i == a - 1:   
        print("* " * b)
    else:                         
        print("* *")

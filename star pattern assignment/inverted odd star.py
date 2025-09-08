#inverted odd star 
n=int(input("enter row:"))
for i in range(n, 0, -1):   # start from n down to 1
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
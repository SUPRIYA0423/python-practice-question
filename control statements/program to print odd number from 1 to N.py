#print odd numbers from  1 to N
N = int(input("Enter the number: "))
i = 1
while i <= N:
    if i % 2 != 0:
        print(i)
    i += 1
#print even numbers from 1 to N
a = int(input("Enter the number: "))
i = 1
while i <= a:
    if i % 2 == 0:
        print(i)
    i += 1
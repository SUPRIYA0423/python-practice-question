#checking if number b is present in A
a = list(map(int, input("Enter the numbers: ").split()))
n=int(input("search number:"))
s=0
for i in range(len(a)):
    if a[i] == n:
        print(i)   
        s = 1

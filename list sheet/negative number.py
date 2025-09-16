#negative number
a=list(map(int,input("enter the numbers:").split()))
for num in a:
    if num < 0:
        print(num)

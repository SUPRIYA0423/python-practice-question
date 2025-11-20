def square(x,y):
    for num in range(x,y+1):
        print(num,num*num)
        
x = int(input("Enter x: "))
y = int(input("Enter y: "))

print(square(x, y))

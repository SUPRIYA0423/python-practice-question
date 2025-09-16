#given an array cumpute the sum of all elements
A = input()
total = 0
numbers = list(map(int, A.split()))
for num in numbers:
    total += num
    print("sum of elements is:",total)
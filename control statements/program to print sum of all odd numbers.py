#sum of all odd number 
A=int(input("enter the number:"))
odd=0
i=1
while i < A:
  odd += i
  i += 2 
  print("Sum of odd numbers from 1 to", A, "is:",odd)
#even odd list
a=list(map(int,input("enter the numbers:").split()))
even=0
odd=0
for num in a:
    if num % 2 == 0:
        even +=1
    else:
        odd +=1    
if even > odd:
    diff = even - odd
else:
    diff = odd - even

print("Difference =", diff)
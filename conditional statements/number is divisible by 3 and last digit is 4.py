# to check number is divisible by 3 and last digit is 4
c=int(input("enter the number:"))
if c%3==0 and c%10==4:
    print("yes it is divisible by 3 and last digit is 4")
else:
    print("no it is not divisible by 3 and last digit is also not 4")
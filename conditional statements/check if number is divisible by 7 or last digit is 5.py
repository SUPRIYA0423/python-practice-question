#WAP to check if number is divisible by 7 or if the last digit is 5
d=int(input("enter the number:"))
divide_by_7= d%7==0
last_digit=d%10==5
if divide_by_7 and last_digit:
    print("number is divisible 7 and last digit is 5")
else:
    if not divide_by_7:
        print("number is not divide by 7")
    if not last_digit:
            print("last digit is not 5")
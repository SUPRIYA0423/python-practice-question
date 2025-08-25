#palindrome code
A = int(input("Enter A: "))
original = A
reverse = 0
if A < 0:
    print("No")
else: 
    while A > 0:
        digit = A % 10
        reverse = reverse * 10 + digit
        A = A // 10
    if original == reverse:
        print("Yes it is palindrome")
    else:
        print("No it is not palindrome")
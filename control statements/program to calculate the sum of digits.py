#sum of digits of given numbers
N = int(input("Enter an integer: "))
digit_sum = 0
if N < 0:
    N = -N
while N > 0:
    digit = N % 10        
    digit_sum += digit    
    N = N // 10            

print("Sum of digits:", digit_sum)
# Grade percentage
a = float(input("Enter the percentage: "))
if a < 25:
    grade = "D"
elif a <= 45:
    grade = "C"
elif a <= 65:
    grade = "B"
elif a <= 85:
    grade = "A"
else:
    grade = "A+"
print("Grade is:", grade)
#string operation
A="aeiOUz"
concat=A+A
upper=""
for char in concat:
    if "a" <= char <= 'z':
        upper += char
r=""
vowels = "aeiou"
for char in upper:
    if char in vowels:
        r += '#'
    else:
        r += char
print(r)
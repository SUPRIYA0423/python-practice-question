#using to upper() in string
t= ("pYthON")
upper = ""
for char in t:
    if 'a' <= char <= 'z':
        upper += chr(ord(char) - 32)
    else:
        upper += char
print(upper)
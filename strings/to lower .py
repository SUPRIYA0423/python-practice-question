#strng to lower()
t= ("PythoN")
lower = ""
for char in t:
    if 'A' <= char <= 'Z':
        lower += chr(ord(char) + 32)
    else:
        lower += char
print(lower)
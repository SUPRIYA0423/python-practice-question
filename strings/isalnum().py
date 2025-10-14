#isalnum()
a=input()
f=1
for ch in a:
    if not (ch.isalnum()):
        f=0
        break
print(f)
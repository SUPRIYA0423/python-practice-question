#count occurence
# a="abobobc"
# occur=a.count("bob")
# print(occur)

a="abobobc"
substring="bob"
count=0
n=len(substring)
for i in range(len(a)-n+1):
    if a[i:i+n] == substring:
        count += 1
print(count)


#first occurence of word
A="aabababaa"
B="ba"
n=len(A)
m=len(B)
for i in range(n-m+1):
    if A[i:i+m] == B:
        print(i)
        break
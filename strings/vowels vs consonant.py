T=int(input())
for i in range(T):
    s=input()
    vowel=0
    consonant=0
    for ch in s:
        if ch.lower() in 'aeiou':
            vowel += 1
        else:
            consonant += 1
    print(vowel,consonant)

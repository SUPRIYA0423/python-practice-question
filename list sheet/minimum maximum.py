#given an array find the maximum and minimum  value in it. 
n=input()
arr=list(map(int,n.split())) 
answer = -float("inf")
answer1 = float("inf")
for i in arr:
     if (i>answer):
        answer = i
     if i<answer1: 
         answer1 = i  
print("maximum value is:",answer)  
print("minimum value is:",answer1)   
import math
def sumDigits(n):
    sum=0
    while n:
        sum+=(n%10)
        n//=10
    return sum
max=0
for i in range(2,100):    
    for j in range(1,100):
        k=i
        for l in range(1,j):
            k=k*i
        sumd=sumDigits(k)
        if sumd>max:
            max=sumd

print max
        

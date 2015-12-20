import math
def checkSqr(n):
    return math.sqrt(n)<int(math.sqrt(n))+0.000001

p=[0 for x in range(1001)]
max=0
for i in range(1,1000):
    for j in range(1,1000):
        k=(i*i)+(j*j)
        if checkSqr(k):
            sum=i+j+int(math.sqrt(k))
            if sum<1001:
                p[sum]+=1
                if p[sum]>p[max]:                    
                    max=sum

print max

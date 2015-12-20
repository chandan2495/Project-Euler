import math
#prime numbers sieve algorithm
n=100001
a=[0 for x in range(n)]
a[0]=a[1]=1
for i in range(2,int(math.sqrt(n))):
    if a[i]==0:
        j=i*i
        while j < n:
            a[j]=1
            j+=i

def checkSqr(n):
    return math.sqrt(n)<int(math.sqrt(n))+0.000001

p=[]
for i in range(n):
    if a[i]==0:
        p.append(i)
flag=0
for i in range(3,n):
    if a[i]==1 and i%2!=0:
        j=0
        flag=0
        while p[j]<i and j<len(p):
            dif=i-p[j]
            dif=dif/2            
            if dif>0 and checkSqr(dif):
                flag=i
                break
            j+=1
        if flag==0:
            break
print i
print p[:100]

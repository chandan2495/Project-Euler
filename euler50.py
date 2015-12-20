from math import sqrt
a=[0 for x in range(1000100)]

a[0]=a[1]=1
for i in range(2,int(sqrt(1000100))):
    if a[i]==0:
        j=i*i
        while j<=1000000:
            a[j]=1
            j+=i
print 'primes are done'
sum=0
for i in range(2,1000):
    if a[i]==0:
        sum+=i
    if sum==953:
        break

print sum


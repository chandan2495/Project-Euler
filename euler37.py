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
for i in range(2,1000000):
    if a[i]==0:
        print i ,

sum=0
count=0
for i in range(11,1000000):
    if a[i]==0:
        #print i
        temp=i
        digitc=0
        while temp>0:
            digitc+=1
            temp=temp/10
            if a[temp]==0:
                continue
            else:
                break

        if temp==0:
            temp=i
            digitc-=1
            while temp>0:
                p=10**digitc
                digitc-=1
                temp=temp-(temp/p)*p
                if a[temp]==0:
                    continue
                else:
                    break

            if temp==0:
                
                count+=1
                print '%d - %d' %(count,i)
                sum+=i

print sum            
        

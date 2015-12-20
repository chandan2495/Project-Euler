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
'''
for i in range(2,1000000):
    if a[i]==0:
        print i ,
'''
def list_to_number(a):
    n=0
    for i in a:
        n=n*10+i
    return n

def number_to_list(n):
    a=[]
    while n>0:
        a.append(n%10)
        n=n/10
    a=a[::-1]
    return a

sum=0
count=0
for i in range(11,1000000):
    if a[i]==0:
        #print i
        temp=number_to_list(i)
        n=len(temp)
        for j in range(n):
            c=temp[0]
            temp=temp[1:n]
            temp.append(c)
            num=list_to_number(temp)
            #print num , 
            if(num<=1000000):
                if a[num]==0:
                    continue
                else:
                    break
            else:
                break
        if j==n-1:
            print i
            count+=1
                
print count+4            
        

a=[0 for x in range(100010)]
b=[0 for x in range(100010)]
sum=0
x=0
y=0

def cal(n):
    sum1=0
    for i in range(1,(n/2)+1):
        if n%i==0:
            sum1+=i
    return sum1

for i in range(1,10001):
    if a[i]!=0:
        x=a[i]
    else:
        x=a[i]=cal(i)
    if a[x]!=0:
        y=a[x]
    else:
        y=a[x]=cal(x)

    if y==i and i!=x:
        sum+=i
        print i

print sum
        
            

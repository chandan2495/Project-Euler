fact=[1,1,2,6,24,120,720,5040,40320,362880]

ans=0
for i in range(10,10000001):
    temp=i
    sum=0
    while temp>0:
        sum+=fact[temp%10]
        temp/=10
    if i==sum:
        ans+=i

print ans
        

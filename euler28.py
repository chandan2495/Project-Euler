n=1001
a=[[0 for x in range(n)] for x in range(n)] #initializing a two dimensional array
inc=1
x=n/2
y=n/2
c=1
a[x][y]=c
c+=1
for i in range(n/2):
    for j in range(inc):
        x+=1
        a[x][y]=c
        c+=1

    for j in range(inc):
        y+=1
        a[x][y]=c
        c+=1
    inc+=1
    for j in range(inc):
        x-=1        
        a[x][y]=c
        c+=1        
    for j in range(inc):
        y-=1
        a[x][y]=c
        c+=1        
    inc+=1
a=zip(*a)
#for i in a:
#    print i
sum=0
for i in range(n):
    #print a[i][i]
    sum+=a[i][i]
j=0;k=n-1
for i in range(n):
    #print a[j][k]
    sum+=a[j][k]
    k-=1
    j+=1

print sum

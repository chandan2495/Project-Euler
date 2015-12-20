import sys
def digits(n):
    ar=[]
    while n:
        ar.append(n%10)
        n/=10
    return ar

def gcd(a,b):
    return gcd(b,a%b) if b!=0 else a

def getnewratio(a,b):
    if (a[0]==b[0] and a[1]!=b[1]):
        d=int(a[1])
        e=int(b[1])
    if (a[0]==b[1] and a[1]!=b[0]):
        d=int(a[1])
        e=int(b[0])
    if (a[1]==b[0] and a[0]!=b[1]):
        d=int(a[0])
        e=int(b[1])
    if (a[0]!=b[0] and a[1]==b[1]):
        d=int(a[0])
        e=int(b[0])
    return d,e
        


#print gcd(int(sys.argv[1]),int(sys.argv[2]))

count=0
for i in range(11,100):
    for j in range(i+1,100):
        a=digits(i)
        b=digits(j)
        if i%10!=0 and j%10!=0 and(a[0]==b[0] and a[1]!=b[1]) or (a[0]==b[1] and a[1]!=b[0]) or (a[1]==b[0] and a[0]!=b[1]) or (a[0]!=b[0] and a[1]==b[1]):
            d,e=getnewratio(a,b)
            nde=gcd(d,e)
            nij=gcd(i,j)
            d=d/nde
            e=e/nde
            ii=i/nij
            jj=j/nij
            if ii==d and jj==e:
                print i,'/',j
                print d,'/',e
                count+=1
            if count==4:
                break
    if count==4:
        break

print count
                
                
            

def lasttendigits(n):
    ar=[]
    i=0
    while n and i<10:
        ar.append(n%10)
        n/=10
        i+=1
    return ar[::-1]

def numFDigits(ar):
    n=0
    for i in ar:
        n=n*10+int(i)
    return n
n=2
for i in range(2,7830458):
   n=n*2
   ar=lasttendigits(n)
   n=numFDigits(ar)

print n*28433

def digits(a):
    arr=[]
    while a:
        arr.append(a%10)
        a=a/10
    return arr

def matchDigits(a,b):
    aDigits=digits(a)
    bDigits=digits(b)
    aDigits.sort()
    bDigits.sort()
    return aDigits==bDigits

n=1
while 1:
    if matchDigits(n,2*n) and matchDigits(n,3*n) and matchDigits(n,4*n) and matchDigits(n,5*n) and matchDigits(n,6*n):        
        break
    n+=1
print n
print 2*n
print 3*n
print 4*n
print 5*n
print 6*n


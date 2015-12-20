def digits(a):
    arr=[]
    while a:
        arr.append(a%10)
        a=a/10
    return arr
def numFromDigits(a):
    n=0
    for i in a:
        n=n*10+int(i)
    return n

count=0
for a in range(2,10001):
    n=a
    for i in range(50):
        rDigits=digits(n)
        aDigits=rDigits[::-1]
        sum=numFromDigits(rDigits)+numFromDigits(aDigits)
        sDigits=digits(sum)
        if sDigits==sDigits[::-1]:            
            break
        n=sum
    if i>=49:
        count+=1
        
print count


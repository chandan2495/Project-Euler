ar=[]
n=0
sum=0
c=0

with open('input.txt') as f:
    while True:
        a=f.read(1)
        if not a:
            break
        if a<'0' and a>'9':
            continue
        else:
            c+=1
            if c==151:
                ar.append(n)
                n=0
                c=1
            a=ord(a)-ord('0')
            n=n*10+a

ar.append(n)

for i in ar:
    print '---------------'
    print i
    sum+=i

print sum
print len(ar)

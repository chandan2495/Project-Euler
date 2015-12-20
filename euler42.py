import os
f=open('euler42words.txt','r')
t=f.read()
t=t.replace('\"','')
a=t.split(',')
tnums=[]
sum=0
for i in range(1,10000):
    sum+=i
    tnums.append(sum)

def search(n):
    for i in tnums:
        if i==n:
            return 1
    return 0

count=0
for word in a:
    sum=0
    for c in word:
        sum+=ord(c)-65+1
    print sum
    if search(sum):
        count+=1

print count

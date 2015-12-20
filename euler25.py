
def digitcount(n):
    count=0
    while n>0:
        count+=1;
        n/=10
    return count

count=2
f=1
s=1
t=0
while True:
    t=s
    s=f+s
    f=t
    if digitcount(s)==1000:
        break
    count+=1

print count
print s


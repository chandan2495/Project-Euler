arr=[]
for a in range(2,101):
    for b in range(2,101):
        arr.append(pow(a,b))

b=set(arr)
print len(b)

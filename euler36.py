def base2(a):
    arr=[]
    while a:
        arr.append(a%2)
        a=a/2
    arr=arr[::-1]
    return arr
def digits(a):
    arr=[]
    while a:
        arr.append(a%10)
        a=a/10    
    return arr

def pallin(arr):
    return arr==arr[::-1]

sum=0
for i in range(1,1000000):
    if pallin(digits(i)) and pallin(base2(i)):
        sum+=i

print sum

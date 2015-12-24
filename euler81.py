import os

f=open('euler81matrix.txt')
t=f.read()
lines=t.split('\n')
a=[]
for line in lines:
	if line.strip()!='':
		b=line.split(',')
		a.append(b)
		# print a
m=[ [0 for x in range(81)] for x in range(81)]

k=0
print len(a)
# for i in range(81):
# 	for j in range(81):
# 		m[i][j]=a[k]
# 		k+=1

# print m

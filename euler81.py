import os
a=[]
min1=10000000
def recur(i,j,sum1):
	if i<80 and j<80:		
		# print a[i][j] + ' ' + str(sum1)
		if i==79 and j==79:
			global min1	
			print sum1	
			if sum1<min1:
				min1=sum1	
		if i+1<80:
			recur(i+1,j,sum1+int(a[i+1][j]))
		if j+1<80:
			recur(i,j+1,sum1+int(a[i][j+1]))		

f=open('euler81matrix.txt')
t=f.read()
lines=t.split('\n')
for line in lines:
	if line.strip()!='':
		b=line.split(',')
		a.append(b)
		# print a
# m=[ [0 for x in range(81)] for x in range(81)]
# print a
recur(0,0,int(a[0][0]))
print min1

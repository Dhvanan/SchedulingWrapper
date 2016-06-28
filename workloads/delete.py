import os
os.system('nova list > instances')
f=open('instances','r')
data = f.readlines()
id=[]
for i in data[3:-1]:
	i=i.split('|')
	id.append(i[1])
for i in id:
	os.system('nova delete '+i)

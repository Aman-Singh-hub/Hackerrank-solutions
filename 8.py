def large(x):
	l=[]
	for i in x:
		l.append(int(i))
	m=max(l)
	count=0
	for i in l:
		if(i==m):
			count+=1
	print(count)	













n=int(input())
while(True):
	a =input()
	lst=a.split(" ")
	if(len(lst)!=n):
		print("Again Enter The List With",n,"Numbers")
	else:
		break
large(lst)
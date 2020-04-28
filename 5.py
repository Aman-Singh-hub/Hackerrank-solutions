def plusMinus(l,n):
	p=0.0
	m=0.0
	z=0.0

	for i in l:
		if(float(i)<0):
			m+=1
		if(float(i)>0):
			p+=1
		if(float(i)==0):
			z+=1
	print(p/n)
	print(m/n)
	print(z/n)






n=float(input())
while(True):
	a =input()
	lst=a.split(" ")
	if(len(lst)!=n):
		print("Again Enter The List With",n,"Numbers")
	else:
		break
plusMinus(lst,n)
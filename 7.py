def comp(l):
	l2=[]
	l3=[]
	for i in l:
		l3.append(int(i))
	s=0
	for i in range(len(l)):
		s=sum(l3)-l3[i]
		l2.append(s)
	print(min(l2),max(l2))
















a =input()
l1=a.split()
comp(l1)


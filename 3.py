def add(x):
	s=0
	for i in x:

		s+=int(i)
	print(s)



  
# number of elemetns as input 
  
# iterating till the range 
n = int(input()) 
  
# iterating till the range 
while(True):
	a =input()
	lst=a.split(" ")
	if(len(lst)!=n):
		print("Again Enter The List With",n,"Numbers")
	else:
		break

add(lst)

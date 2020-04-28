def simpleArraySum(ar):
    s=0
    for i in ar:
        s=s+int(i)
    print(s)
    #
    # Write your code here.
    #
lst = [] 
  
# number of elemetns as input 
n = int(input()) 
  
# iterating till the range 
while(True):
	a =input()
	lst=a.split(" ")
	if(len(lst)!=n):
		print("Again Enter The List With",n,"Numbers")
	else:
		break


simpleArraySum(lst)

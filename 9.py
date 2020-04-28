#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
def conv(lst):
	if(lst[-1][2:4]=="PM"):
		if(lst[0]=="12"):
			lst[0]="12"
		else:
			a=int(lst[0])+12
			lst[0]=str(a)
	else:
		if(lst[0]=="12"):
			lst[0]="00"


	b=":".join(lst)
	print(b[0:(len(b)-2)])



a=input()
lst=a.split(":")
conv(lst)
n=int(input())
sp=0
ss=0
	#for primary digonal 11 22 33
for i in range(n):
	a =input()
	b=a.split(" ")
	sp=sp+int(b[i])
	ss+=int(b[-(i+1)])



#for Secondary diagonal 1-1 2-2 3-3
print(abs(sp-ss))




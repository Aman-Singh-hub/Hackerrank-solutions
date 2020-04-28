def winner(x,y):
    alice=0
    bob=0
    for i in range(3):
        if(int(x[i])>int(y[i])):
            alice+=1
        if(int(x[i])<int(y[i])):
            bob+=1
    print(alice,bob)
    
  
# number of elemetns as input 
  
# iterating till the range 
a =input()
l1=a.split()
b=input()
l2=b.split()

winner(l1,l2)

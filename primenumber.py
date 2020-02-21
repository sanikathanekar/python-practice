'''
#Prime number
n=int(input("Enter a number->"))
c=0
i=2

while(i<=(n//2)):
    if(n%i==0):
        c=c+1 
    i=i+1

if (c==0 and n!=1):
    print("{} is a Prime Number".format(n))
else:
    print("{} is not a Prime Number".format(n))
'''

for n in range(1,100):
    s=0 #sum
    c=1 #multiple
    while c<=n:
        if n%c==0:
            s=s+c
        c=c+1
    if s==(n+1):
       print(n)




    
        
    


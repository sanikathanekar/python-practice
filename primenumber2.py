
#Prime number between 1-100

n=1
while n<=100:
    c=0
    i=2
    while i<=n//2:
        if n%i==0:
            c=c+1
        i=i+1

    if c==0 and n!=1:
        print(n)
    n=n+1




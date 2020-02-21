#Perfect number.
'''
A perfect number is an integer that is equal to the sum of its positive divisors excluding itself.
eg. 6 is dividible by 1,2,3 1+2+3=6, So 6 is a perfect number.

n=int(input("number-"))
c=1
s=0
while c<n:
    if n%c==0:
        s=s+c
    c=c+1
if s==n:
    print("{} is a perfect number".format(n))
else:
    print("{} is not a perfect number".format(n))


n=int(input("number-"))
c=1
s=0
while c<n:
    if n%c==0:
        a=n%c
        print("a-",a)
        s=s+c
        print("s-",s)
    c=c+1
    print("c-",c)
if s==n:
    print("{} is a perfect number".format(n))
else:
    print("{} is not a perfect number".format(n))
'''
n=6
m=1
s=0
while m<n:
    if n%m==0:
        s=s+m
    m=m+1
if s==n:
    print("Yes")
else:
    print("No")
        
        

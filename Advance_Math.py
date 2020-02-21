
#Factorial
def Factorial(n):
    if n==1:
        return 1
    else:
        return(n*Factorial(n-1))

#Prime Number
def PrimeNumber(n):
    s=0
    c=1
    while c<=n:
        if n%c==0:
            s=s+c
        c=c+1
    if s==(n+1):
        return "{} is a Prime Number".format(n)
    else:
        return "{} is not a Prime Number".format(n)

#Reverse Number
def ReverseNumber(n):
    rev = 0
    while n!=0:    
        rem = n %10    
        rev = (rev*10) + rem   
        n = n //10
    return(rev)
#Armstrong Number
def Armstrong(n):
    num=n
    rem=0
    arm=0
    while num!=0:
        rem=num%10
        arm=arm+(rem**3)
        num=num//10
    if n==arm:
        return"{} is an armstrong number".format(n)
    else:
        return"{} is not an armstrong number".format(n)

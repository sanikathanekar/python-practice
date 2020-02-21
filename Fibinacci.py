#Write a program to print fibonacci sereies between 1 to 10.
'''
Fibonacci series is a series of numbers in which each number is the sum of preceeding numbers.
n1= First number
n2= Second number
n3= Next number


n1=0
n2=1
n3=0
while n1<=10:
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3
    
'''

n1=0
n2=1
n3=0
while n1<=10:
    print(n1)
    n3=n1+n2
    print("n3-",n3)
    n1=n2
    print("n1-",n1)
    n2=n3
    print("n2-",n2)

n1=0
n2=1
n3=0
while n1<=10:
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3

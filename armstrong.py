#Write a program to check if the given number is armstrong or not.Number=123
'''
Armstrong number is a number that is equal to the sum of the cubes of its own digits.
eg. 153
1*1*1+5*5*5+3*3*3=153
'''

num=int(input("Number-"))
n=num
rem=0
arm=0
while n!=0:
    rem=n%10
    arm=arm+(rem**3)
    n=n//10
if num==arm:
    print("{} is an armstrong number".format(num))
else:
    print("{} is not an armstrong number".format(num))
    
'''  

n=int(input("Number-"))
num=n
rem=0
arm=0
while n!=0:
    print("before n-",n)
    rem=n%10
    print("rem-",rem)
    arm=arm+(rem**3)
    print("arm-",arm)
    n=n//10
    print("n-",n)
if num==arm:
    print("Yes")
else:
    print("no")
'''

n=int(input("Number-"))
num=n
arm=0
rem=0
while n>0:
    rem=n%10
    arm=arm+(rem**3)
    n=n//10
if arm==num:
    print("Num is arm")
else:
    print("Num is noyt")
    arm=

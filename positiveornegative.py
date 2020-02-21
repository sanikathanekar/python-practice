#Write a program to check if the user entered number is positive negative or 0.

n=int(input("Enter Number->"))
if n>0:
    print("{} is positive".format(n))
elif n<0:
    print("{} is negative".format(n))
else:
    print("Number is 0".format(n))


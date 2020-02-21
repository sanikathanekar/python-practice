'''
# Write a program to find the factorial of function by recursion.


def Factorial(n):
    if n==1:
        return 1
    else:
        return(n*Factorial(n-1))

num=int(input("Enter Number-"))

print(Factorial(num))
'''

def Square(n):
    if n==1:
        return 1
    else:
        return n*n

num=int(input("Enter Number-"))
print(Square(num))

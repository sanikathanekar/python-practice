#Write a program to check if the middle number is middle or not.

x=int(input("x-"))
y=int(input("y-"))
z=int(input("z-"))

if x>y and x<z:
    print("x is the middle number".format(x))
elif y>x and y<z:
    print("y is the middle number".format(y))
else:
    print("z is the middle number".format(z))

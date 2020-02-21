'''
Q1.Take values of length and breadth of a rectangle from user
and check if it is square or not.


l=int(input("Enter Length-"))
b=int(input("Enter breadth-"))
if l==b:
    print("the polygon is a square")
else:
    print("the polygon is a rectangle")


Q2. Take two int values from user and print greatest among them.

a=int(input("Enter a number-"))
b=int(input("Enter a number-"))
if a>b:
    print("{}is greater".format(a))
else:
    print("{}is greater".format(b))

Q3. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount

y=int(input("Years of service-"))
s=int(input("Enter salary-"))
b=((5/100)*s) + s

if y>5:
    print("Bonus is-", b)
else:
    print("Salary-", s)

4)  A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.

s=100
b=200
f=150
while True:
    print("~"*20,"Product Menu","~"*20)
    print("Product","        ","Price")
    print("1-Shampoo","      ",s)
    print("2-Conditioner","  ",b)
    print("3-Facewash","     ",f)
    print("Product"," ","Quantity"," ","Total")
    c=int(input("Select items-"))
    q=int(input("Quantity-"))
    if c==1:
        print("Shampoo","    ",q,"         ",i*q)
    elif c==2:
        print("Conditionar"," ",q,"        ",i*q)
    elif c==3:
        print("Facewash","    ",q,"        ",i*q)
    else:
        print("Select a valid product")
        print("~"*50)
    ch=input("Would you like to continue shopping-")
    if ch=='y' or ch=='Y':
        continue
    else:
        print("Thankyou for Shopping")
        break


Q. Take input of age of 3 people by user and
determine oldest and youngest among them.

a=int(input("Enter sam's age-"))
b=int(input("Enter ron's age-"))
c=int(input("Enter billi's age-"))
if a>b and a>c:
    print("Sam is oldest")
elif b>a and b>c:
    print("Ron is oldest")
else:
    print("Billi is oldest")

if a<b and a<c:
    print("Sam is youngest")
elif b<a and b<c:
    print("Ron is youngest")
else:
    print("Billi is youngest")
'''
a=int(input("Enter Number-"))
if a<0:
    a=a*(-1)
    print(a)
else:
    print(a)



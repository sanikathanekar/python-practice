'''
#Shopping
p=10
b=30
s=5
e=5
r=20

while True:
    print("~"*20,"Product Menu","~"*20)
    print("Product","         ","Price")
    print("1-Pencil","          ",p)
    print("2-Scale","           ",s)
    print("3-Eraser","          ",e)
    print("4-Book","            ",b)
    print("5-Ruler","           ",r)
    print("~"*50)
    c=int(input("Select items-"))
    q=int(input("Quantity-"))
    print("~"*22,"Bill","~"*22)
    print("Product"," ","Quantity"," ","Total")
    if c==1:
        print("Pencil","    ",q,"         ",p*q)
    elif c==2:
        print("Scale","     ",q,"         ",s*q)
    elif c==3:
        print("Eraser","    ",q,"         ",e*q)
    elif c==4:
        print("Book","      ",q,"         ",b*q)
    elif c==5:
        print("Ruler","      ",q,"        ",r*q)
    else:
        print("Invalid option. Please select a valid option")
    print("~"*50)
    ch=input("Would you like to continue shopping-")
    if ch=='y' or ch=='Y':
        continue
    else:
        print("Thankyou for Shopping")
        break
'''
a=1000
q=int(input("Quantity-"))
b=a*q
if b>1000:
    print(b)
    print("Amount after discount-", b- ((10/100)*b))
else:
    print("Total bill is-", b)
            


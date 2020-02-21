#calculator

while True:
    print("+ ->Addition")
    print("- ->Subtraction")
    print("* ->Multiplication")
    print("/ ->Division")
    print("// ->Floor division")
    print("% ->Modulo")
    print("** ->Exponents")
    print("E ->Exit")
    c=input("Select operation->")
    x=float(input("Enter Number->"))
    y=float(input("Enter Number->"))
    if c=='+':
        ans=x+y
        print("The sum is {}".format(ans))
    elif c=='-':
        ans=x-y
        print("The answer is {}".format(ans))
    elif c=='*':
        ans=x*y
        print("The answer is {}".format(ans))
    elif c=='/':
        ans=x/y
        print("The answer is {}".format(ans))
    elif c=='//':
        ans=x//y
        print("The answer is {}".format(ans))
    elif c=='%':
        ans=x%y
        print("The answer is {}".format(ans))
    elif c=='**':
        ans=x**y
        print("The answer is {}".format(ans))
    elif c=='E' or c=='e':
        print(Exit)
    else:
        print("Select a valid operator")
    break
        
        
    
    

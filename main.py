#calculator
from AdvanceMath import *

def main():
    print("Advance Math Calculator")
    while True:
        print("1 ->Factorial")
        print("2 ->PrimeNumber")
        print("3 ->ReverseNumber")
        print("4 ->Armstrong")
        print("5 ->Exit")
        c=int(input("Select operation->"))
        
        if c==1:
            print("******Factorial******")
            n = int(input("Enter Number-"))
            a=Factorial(n)
            print("Factorial of {}=".format(n),a)
        elif c==2:
            print("******Prime or not******")
            n = int(input("Enter Number-"))
            a=PrimeNumber(n)
            print(a)
        elif c==3:
            print("******ReverseNumber******")
            n = int(input("Enter Number-"))
            a=ReverseNumber(n)
            print("The reverse of {}=".format(n),a)
        elif c==4:
            print("******Armstrong or not******")
            n = int(input("Enter Number-"))
            a=Armstrong(n)
            print(a)
        elif c==5:
            break
        else:
            print("Select a valid operator")
            
if __name__ == '__main__':
    main()


def main():
    print("File Operations Menu")
    while True:
        print("1 ->Read")
        print("2 ->Write")
        print("3 ->Delete")
        print("4 ->Rename")
        print("5 ->Copy")
        print("6 ->Exit")
        c=int(input("Select operation->"))
        if c==1:
            print("******Read******")
            file=input("File Name-")
            f=open(file,"r")
            print(f.read())
            f.close()
        elif c==2:
            print("******Write******")
            file=input("File Name-")
            f=open(file,"w")
            w=input("Enter your thoughts-")
            print(f.write(w))
            f.close()
        elif c==3:
            print("******Delete******")
            f=input("Enter file name-")
            import os
            os.remove(f)
            print("File sucessfully removed")
        elif c==4:
            print("******Rename******")
            f=input("Enter file name-")
            n=input("Rename as-")
            import os
            os.rename(f,n)
            print("{} renamed".format(f))
        elif c==5:
            print("******Copy******")
        elif c==5:
            break
        else:
            print("Select a valid operator")
            
if __name__ == '__main__':
    main()

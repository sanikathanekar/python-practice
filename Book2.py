class Book:
    def __init__(self,bid,bname,price):
        print("Book object created")
        self.bid=bid
        self.bname=bname
        self.price=price

    def printBook(self):
        print("Book ID:{0}\nBook Name:{1}\nBook Price:{2}".format(self.bid,self.bname,self.price))

def Menu():
    b1=Book(1,"Hobbit",300)
    b2=Book(2,"Lord Of The Rings",350)
    b3=Book(3,"Game Of Thrones",500)
    b1.printBook()
    b2.printBook()
    b3.printBook()

def bookList():
    blist=list(b1,b2,b3)
    print("Book List:",blist)

if __name__=='__main__':
    Menu()


while True:
    print("***********************Book System**************************")
    print(blist)
    print("1. Add Book")
    print("2. Update Book")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Show list of Books")
    ch=int(input("Select an option:"))

    if ch==1:
        print("Add Book")

    break

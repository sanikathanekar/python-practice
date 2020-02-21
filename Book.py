class Book:
    
    def __init__(self):
        print("Book object created")

    
    def createBook(self):
        self.bid=input("Book ID-")
        self.bname=input("Book Name-")
        self.price=input("Book Price-")

    
    def subscription(self, month):
        return month*self.price
    
    def printBook(self):
        print("Book ID:",self.bid)
        print("Book Name:",self.bname)
        print("Book Price:",self.price)

    def __str__(self):
        return "bid: {0}, bname: {1}, price: {2}".format(self.bid, self.bname, self.price)




    
booklist=list()
# print("1 Book list",booklist)

def ashish():
    b1 = Book1(123,"got",100)
    b2 = Book1(32, "rs", 200)
    b1.printBook()
    b2.printBook()

class Book1:
    def __init__(self, bid, bname, price):
        self.bid = bid
        self.bname = bname
        self.price = price

    def printBook(self):
        print('bid:{0}, bname:{1}, price:{2}'.format(self.bid,self.bname,self.price))
              
def sanika():

    while  True:
        print("***********************Book System**************************")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Show list of Books")

# #2424. b1 | Book() bid 1;bname="song of fire and ice"; price=$10000 
#   |
# #232    b2| Book()
#   |

        
        print("6. Exit")
        ch=int(input("Enter choice-"))

        if ch==1:
            b1=Book()
            
            b1.createBook()
            #booklist=[b1]
            booklist.append(b1) 
            print("Book added successfully to the list")
            print("2 B list-",booklist)

        elif ch==2:
            pass
        elif ch==3:
            i=input("Enter book Name-")
            for n in booklist:
                if i==n:
                    print("Book present")
                else:
                    print("Book not found")
            pass
        elif ch==4:
            pass
        elif ch==5:
            for l in booklist:
                l.printBook()
        elif ch==6:
            break
        else:
            print("Choice not available")


if __name__=='__main__':
     ashish()
        

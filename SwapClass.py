class Swapping:
    def __init__(self):
        self.x=int(input("X-"))
        self.y=int(input("Y-"))

    def swap(self):
        self.x=self.x+self.y
        self.y=self.x-self.y
        self.x=self.x-self.y
        print("X-",self.x)
        print("Y-",self.y)

def main():
    d=Swapping()
    d.swap()

if __name__=='__main__':
    main()

    

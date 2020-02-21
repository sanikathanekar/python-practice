
class Robot:
    def __init__(self):
        self.name=input("Enter a Name-")
    def functions(self):
        self.talk=self.name,"Hi I Can Talk"
        self.walk=self.name,"HI I Can Walk"

def main():
    R1=Robot()
    R1.name()
    R1.functions()

if __name__=='__main__':
    main()

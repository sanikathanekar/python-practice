
class student:

    def __init__(self):
        #public
        self.rollno=input("Roll No.-")
        #protected
        self.__name=input("Enter Name-")
        #private
        self.__course=input("Enter course-")

    def printData(self):
        print("Roll No.-",self.rollno)
        print("Enter Name-",self.__name)
        print("Enter course-",self.__course)

    def __del__(self):
        print("Student Deleted")

def main():
    s1=student()
    s1.printData()
    print("Printing Data Outside class")
    try:
        print("Roll No.-",s1.rollno)
        print("Enter Name-",s1.__name)
        print("Enter course-",s1.__course)
    except:
        print("The data is Private")
if __name__=='__main__':
    main()

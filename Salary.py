class Employee:
    def __init__(self):
        self.name=input("Name-")
        self.post=input("Designation-")
        self.salary=int(input("Salary-"))

    def salaryCheck(self):
        try:
            if self.salary<10000:
                raise LowSalary("Alert! Low Salary")
        except LowSalary as e:
            print(e)

class LowSalary(Exception):
    pass

def main():
    c1=Employee()
    c1.salaryCheck()

if __name__=='__main__':
    main()
    

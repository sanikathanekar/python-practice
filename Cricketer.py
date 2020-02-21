class Cricketer:
    def __init__(self,name,byear):
        self.name=name
        self.byear=byear
    def Age(self):
        import datetime
        from datetime import date
        d=int(input("Enter day-"))
        m=int(input("Enter month-"))
        y=int(input("Enter year-"))
        dob=datetime.date(y,m,d)
        print(dob)
        dt=date.today()

        a=dt-dob
        print("Days-",a)
        age=a.days//365
        print("age-",age)
        

def main():
    s=Cricketer("Sachin",1973)
    print("Name-",s.name)
    print("Birth Year-",s.byear)
    s.Age()
    v=Cricketer("Virat",1988)
    print("Name-",v.name)
    print("Birth Year-",v.byear)
    v.Age()

if __name__=='__main__':
    main()





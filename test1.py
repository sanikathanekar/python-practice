# Create a Program for user to get information about Schools present in this area

# School -> id,name,location


class School:
    def __init__(self):
       self.id = input('id:')
       self.name= input('name:')
       self.location= input('location:')

    def printSchool(self):
        print('sid:{0}, sname:{1}, location:{2}'.format(self.id,self.name,self.location))

    
def main():
    s1 = School()
    s2 = School()

    
if __name__=='__main__':
    main()

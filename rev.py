'''
 #Printing rev

num = int(input("Enter a Number->"))    
rev = 0    
while num!=0:    
    rem = num %10    
    rev = (rev*10) + rem   
    num = num //10
print(rev)

'''


num = int(input("Enter a Number->"))
n=num
rev = 0    
while num!=0:    
    rem = num %10    
    rev = (rev*10) + rem   
    num = num //10
if n == rev:
    print("p")
else:
    print("N")

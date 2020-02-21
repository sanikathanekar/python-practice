
class PhoneException(Exception):
   pass 

def Number():
    x=input("Enter Number-")
    if len(x)!=10:
        raise PhoneException("Invalid number")
   
Number()



    

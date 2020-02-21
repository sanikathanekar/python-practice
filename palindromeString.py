'''
string=raw_input("Enter string:")
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")
'''
def palindrome(s):
    return s[::-1]

s=input("Input String-")
if s==palindrome(s):
    print("The string is palindrome")
else:
    print("The string is not palindrome")

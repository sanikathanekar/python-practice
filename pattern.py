'''
*
**
***
****
*****

i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1
'''
'''
Printing pattern mentioned below

      *
    *   *
  *       *
*           *   
  *       *
    *   *
      *
'''

for i in range(7):
    for j in range(7):
        if i+j==3 or j-i==3 or i-j==3 or i+j==9:
            print("*", end="")
        else:
            print(end=" ")
    print() 
'''
      *
    *   *
  *       *
    *   *
      *
'''
for i in range(5):
    for j in range(5):
        if i+j==2 or j-i==2 or i-j==2 or i+j==6:
            print("*", end="")
        else:
            print(end=" ")
    print() 

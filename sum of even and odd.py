'''
Consider a list of numbers nums = [-1 , 14 , 23 , 0 , 2 , -9 , 19 , -8 , 3 ].
Find the sum of even numbers and lowest odd number in the list.
'''

l=[-1 , 14 , 23 , 0 , 2 , -9 , 19 , -8 , 3 ]
e=0
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
        e=e+i
print("Even list-",even)
print("The sum of all even numbets in the list is-",e)

for i in l:
    if i%2!=0:
        odd.append(i)
print("Odd list-",odd)
odd.sort()

sum=e+odd[1]
print("The sum of all even numbers and the lowest odd number is-",sum)

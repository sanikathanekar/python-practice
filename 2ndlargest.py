'''
Consider a list of numbers nums = [-1 , 14 , 23 , 0 , 2 , -9 , 19 , -8 , 3 ].
Find the second highest number the list.
'''

l=[-1 , 14 , 23 , 0 , 2 , -9 , 19 , -8 , 3 ]
print("List-",l)
l.sort()
print("Second highest number in the list is-",l[-2])

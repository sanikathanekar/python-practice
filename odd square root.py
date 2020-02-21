import math as m
l=[]
s=[]
i=0
for n in range(1,20):
    if n%2!=0:
        l.append(n)
        i=m.sqrt(n)
        s.append(i)
print("List of odd numbers from 1 to 20 are->",l)
print("List square roots of odd numbers between 1 to 20 are->",s)


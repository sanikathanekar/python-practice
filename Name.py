# Write a program to print your full name in python.

#print("Sanika Milind Thanekar")
n=int(input("No="))
m=1
s=0
while m<=n:
    if n%m==0:
        s=s+m
    m=m+1
if s==(n+1):
    print("y")
else:
    print("n")

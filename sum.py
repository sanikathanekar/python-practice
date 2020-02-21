#Sum of first 100 numbers.

n=0
s=0
while n<=100:
    s=s+n
    n=n+1
print("The sum of first 100 numbers is {}".format(s))

n=0
s=0
for i in range(1,101):
    s=s+i
print(s)

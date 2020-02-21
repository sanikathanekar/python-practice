# Leap Year

y=int(input("Enter a year ->"))
if y%4==0 and y%100!=0 or y%400==0:
    print("The year {} is a leap year".format(y))
else:
    print("The year {} is not a leap year".format(y))

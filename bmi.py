# Body Mass Index

w=float(input("Enter Weight in Kilogram-"))
h=float(input("Enter Height in Meters-"))
bmi= w/(h**2)
print("BMI-{}".format(bmi))
if bmi<18:
    print("Underweight")
elif bmi>=18 and bmi<=22.5:
    print("Normal")
elif bmi>22.5 and bmi<=25:
    print("Overweight")
else:
    print("Obese")
        

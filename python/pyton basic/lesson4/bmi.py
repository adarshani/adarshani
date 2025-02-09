h = float(input("Enter your height in centimeters: "))
w = float(input("Enter your weight in kilograms: "))

BMI = w / (h/100)**2

print("Your BMI is: ",BMI)

if BMI <= 18.5:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are normal weight")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("your severly overweight")
else:
    print("You are obese")


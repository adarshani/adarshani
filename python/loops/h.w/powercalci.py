basa = int(input('Enter the base'))
exponent = int(input("Enter the exponent: "))

result = 1

for i in range(exponent):
    result = result*basa

print(f"{basa} raised to the power of {exponent} is:{result}")
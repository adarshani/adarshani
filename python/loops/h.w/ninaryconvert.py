# Function to convert decimal to binary
def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    
    binary_number = ""
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
    
    return binary_number

# Function to display binary conversion of numbers using nested loops
def display_binary_conversions(limit):
    for num in range(limit + 1):
        binary_representation = decimal_to_binary(num)
        print(f"Decimal: {num} -> Binary: {binary_representation}")

# Input: Limit for binary conversion
limit = int(input("Enter the limit for binary conversion: "))
display_binary_conversions(limit)

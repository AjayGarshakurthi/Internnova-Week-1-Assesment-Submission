# Task 4: Operators in Python


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
    modulus = num1 % num2
else:
    division = "Not possible (division by zero)"
    modulus = "Not possible (division by zero)"

exponent = num1 ** num2


print("\n----- Calculator Results -----")

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)
print("Exponent:", exponent)
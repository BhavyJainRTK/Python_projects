# Write a program that:

# Takes two integers as input

# Prints their sum, difference, product, and quotient

# Checks if the first number is greater than the second

# Verifies if the numbers are equal using is operator

# Checks if the first number exists in a list [10, 20, 30, 40, 50]

num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
list = [10, 20, 30, 40, 50]

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print("sum > ",sum)
print("difference > ",difference)
print("product > ",product)
print("quotient > ",quotient)

print("First number is greater then second number > ",(num1 > num2))

print("Number are equal > ",(num1 is num2))

print("First number is in the list > ",(num1 in list))
print(type(list))

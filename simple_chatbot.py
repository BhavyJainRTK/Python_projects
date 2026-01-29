print("Hello!  I am your simple chatbot ")

name = input("What is your name? ")
print("Nice to meet you,", name)

print("\nWhat type of help do you want from me? ")
print("Options: add, subtract, multiply, divide")

operation = input("Enter operation: ").lower()

count = int(input("\nHow many numbers do you want to use? "))

numbers = []

for i in range(count):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

result = numbers[0]

if operation == "add":
    result = sum(numbers)

elif operation == "subtract":
    for i in range(1, count):
        result -= numbers[i]

elif operation == "multiply":
    result = 1
    for num in numbers:
        result *= num

elif operation == "divide":
    for i in range(1, count):
        if numbers[i] != 0:
            result /= numbers[i]
        else:
            print("Error: Division by zero ")
            result = None
            break

else:
    print("Invalid operation ")
    result = None

if result is not None:
    print("\nResult:", result)

print("\nThank you for using the chatbot  Have a great day!")
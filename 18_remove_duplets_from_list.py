n = int(input("How many numbers you want to enter > "))

numbers = []
f_number = []

for i in range (0,n):
    numbers.append(input(f"Enter {i+1} number > "))

f_number = list(set(numbers))
f_number.sort()

print(f_number)

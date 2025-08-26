print("Enter five single digit number")

number = []

number.append(input("Enter 1st number > "))
number.append(input("Enter 2nd number > "))
number.append(input("Enter 3rd number > "))
number.append(input("Enter 4th number > "))
number.append(input("Enter 5th number > "))

cp_number = number.copy()
cp_number.reverse()
 
if(cp_number == number):
    print("number is palindrome")
else:
    print("number is not palindrome")
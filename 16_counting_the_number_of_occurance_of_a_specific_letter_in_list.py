print("Enter five letters")

letters = []

letters.append(input("Enter 1st letter > "))
letters.append(input("Enter 2nd letter > "))
letters.append(input("Enter 3rd letter > "))
letters.append(input("Enter 4th letter > "))
letters.append(input("Enter 5th letter > "))

s_letter = input("letter you want to count > ")

print(letters.count(s_letter))
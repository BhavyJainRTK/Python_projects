marks = float(input("Enter your marks : "))

if((marks >= 90)and(marks < 101)):
    print("GRADE = A",)

elif((marks >= 80)and(marks < 90)):
    print("GRADE = B",)

elif((marks >= 70)and(marks < 80)):
    print("GRADE = C",)

elif((marks >= 0))and(marks < 70):
    print("GRADE = D",)

elif(marks < 0):
    print("Entered wrong marks",)

elif(marks > 100):
    print("please enter marks less than or equal to 100",)
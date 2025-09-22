marks = int(input("Enter your Marks(0-100): "))

if marks >= 90 and marks <= 100:
    grade = 'A'
elif marks < 90 and marks >= 75:
    grade = 'B'    
elif marks < 75 and marks >= 50:
    grade = 'C'
elif marks < 50 and marks >= 0:
    grade = 'F'
else:
    print("Your input is wrong")    
    grade = 0

print("Your grade is", grade)    
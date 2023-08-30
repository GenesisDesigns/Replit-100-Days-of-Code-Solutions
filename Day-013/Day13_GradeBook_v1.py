#Title: Replit Day  - Day13 - GradeBook Builder - Generate Grades and GradeBook - v1

print("Exam Grade Calculator")
print("Computer Science")
print("The maximum points you can receive is 110.")
print()
maxPoints = 110
yourPoints = float(input("How many points did you receive?: "))
grade = yourPoints/maxPoints
gradePercentage = str(round(grade * 100, 2)) + "%"


if grade >= 0.9 and grade <= 1:
  print(f"Your grade is {gradePercentage} and you received an A+!")
elif grade >= 0.8 and grade <= .89:
  print(f"Your grade is {gradePercentage} and you received an A-!")
elif grade >= 0.7 and grade <= .79:
  print(f"Your grade is {gradePercentage} and you received aa B!")
elif grade >= 0.6 and grade <= .69:
    print(f"Your grade is {gradePercentage} and you received a C!")
elif grade >= 0.5 and grade <= .59:
    print(f"Your grade is {gradePercentage} and you received a D!")
else:
    print(f"Your grade is {gradePercentage} and you received a U!")
    print("In other words, you've FAILED!!!")
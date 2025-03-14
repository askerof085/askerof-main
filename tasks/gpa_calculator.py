total_grade = 0
for _ in range(5):
    object_name, object_grade = input("Enter course name and grade: ").split()
    if object_grade == 'A':
        object_grade = 4.0
    elif object_grade == 'B':
        object_grade = 3.0
    elif object_grade == 'C':
        object_grade = 2.0
    elif object_grade == 'D':
        object_grade = 1.0  
    elif object_grade == 'F':
        object_grade = 0.0
    total_grade += object_grade
if total_grade/5 <= 2.0:
    print("You have failed")
elif total_grade/5 <= 3.0:
    print('You needs improvement')
elif total_grade/5 <= 3.5:
    print('You are good student')
else:
    print('You are excellent student with high GPA, Congratulations buddy!')
# Normal koddu 
 
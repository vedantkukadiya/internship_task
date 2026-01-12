#Function-Based Student Result System
def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'
student_marks = {'John': 85, 'Alice': 92, 'Bob': 76, 'Diana': 59}
for student, marks in student_marks.items():
    grade = calculate_grade(marks)
    print(f"{student} has received grade: {grade}")

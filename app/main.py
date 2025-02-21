from student import Student
from grade_calculator import calculate_final_grade
from display import display_student_info

def main():
    name = input("Enter the name of the student: ")
    grades = []
    for i in range(3):
        grade = float(input(f"Enter grade {i+1}: "))
        grades.append(grade)

    # Create Student object with the obtained data
    student = Student(name, grades)
    
    # Calculate final grade
    final_grade = calculate_final_grade(student.grades)

    # Display results
    print("\n--- Student Results ---\n")
    display_student_info(student, final_grade)

if __name__ == "__main__":
    main()
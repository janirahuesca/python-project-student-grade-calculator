from student import Student
from grade_calculator import calculate_final_grade, get_classification
from display import display_student_info

def main():
    students = []

    for i in range(5):
        # Ask for the data required (students' name and grades)
        name = input(f"Enter the name of the student {i+1}: ")
        for j in range(3):
            grades = [float(input(f"Enter grade {j+1}: "))]
        # Create Student object with the obtained data
        students.append(Student(name, grades))

    print("\n--- Student Results ---\n")
    for student in students:
        # Calculate final grade and classification
        final_grade = calculate_final_grade(student.grades)
        classification = get_classification(final_grade)
        # Display results
        display_student_info(student, final_grade, classification)

if __name__ == "__main__":
    main()
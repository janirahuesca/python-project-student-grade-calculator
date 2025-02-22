from views.student_view import StudentView
from controllers.student_controller import StudentController

def main():
    students = []
    num_students = 5

    while len(students) < num_students:
        try:
            # Get the student data (via the view)
            name, grades = StudentView.get_student_data()

            # Process the data (via the controller)
            student, final_grade, classification = StudentController.create_student(name, grades)

            # Store the processed student information
            students.append((student, final_grade, classification))

        except ValueError as e:
            print(f"Error: {e}")

    # Display the results for all students (via the view)
    StudentView.display_header("STUDENTS RESULTS")
    for student, final_grade, classification in students:
        StudentView.display_student_info(student, final_grade, classification)

if __name__ == "__main__":
    main()

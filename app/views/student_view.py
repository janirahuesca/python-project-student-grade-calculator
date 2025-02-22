class StudentView:

    @staticmethod    
    def get_student_data():
        """Requests student data from the user."""
        name = input("Enter the name of the student: ").strip()
        grades = []
        for i in range(3):
            grade = float(input(f"Enter grade {i+1}: "))
            grades.append(grade)
        return name, grades

    def display_student_info(student, final_grade, classification):
        """Displays the student's information."""
        print(f"Name: {student.name}")
        print(f"Final grade: {final_grade:.2f}")
        print(f"Classification: {classification}")
        print("-" * 30)

    @staticmethod
    def display_header(header):
        """Displays a header for the student results."""
        print("=" * 30)
        print(header.center(30))
        print("=" * 30)
    
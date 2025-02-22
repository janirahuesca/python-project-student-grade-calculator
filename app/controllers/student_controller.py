from models.student import Student
from utils.grade_calculator import calculate_final_grade, get_classification
from utils.validations import validate_name, validate_grade

class StudentController:
    """Handles student-related operations."""

    @staticmethod
    def create_student(name, grades):
        """Creates a Student object and calculates their final grade and classification."""
        
        # Validate the name
        if not validate_name(name):
            raise ValueError("Invalid name. Only alphabetic characters are allowed.")
        
        # Validate the grades
        if not all(validate_grade(grade) for grade in grades):
            raise ValueError("Invalid grade. Grades must be between 0 and 10.")

        student = Student(name, grades)
        final_grade = calculate_final_grade(student.grades)
        classification = get_classification(final_grade)
        return student, final_grade, classification

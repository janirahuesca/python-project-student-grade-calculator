def validate_name(name):
    """Validates that the name contains only alphabetic characters."""
    return name.replace(" ", "").isalpha()

def validate_grade(grade):
    """Validates that the grade is a float or integer between 0 and 10."""
    return isinstance(grade, (int, float)) and 0 <= grade <= 10

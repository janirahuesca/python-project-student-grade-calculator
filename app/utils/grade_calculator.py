def calculate_final_grade(grades):
    """Calculates the final grade as the average of the grades."""
    return sum(grades) / len(grades)

def get_classification(final_grade):
    """Returns the grade classification based on the final grade."""
    if final_grade < 5:
        return "FAIL"
    elif 5 <= final_grade < 7:
        return "PASS"
    elif 7 <= final_grade < 9:
        return "GOOD"
    else:
        return "EXCELLENT"
    
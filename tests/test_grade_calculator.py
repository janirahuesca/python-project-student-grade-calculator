import sys
import os

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from utils.grade_calculator import calculate_final_grade, get_classification

def test_calculate_final_grade():
    assert calculate_final_grade([7, 8, 9]) == 8.0
    assert calculate_final_grade([5, 5, 5]) == 5.0
    assert calculate_final_grade([10, 10, 10]) == 10.0

def test_get_classification():
    assert get_classification(4.9) == "FAIL"
    assert get_classification(5) == "PASS"
    assert get_classification(6.9) == "PASS"
    assert get_classification(7) == "GOOD"
    assert get_classification(8.9) == "GOOD"
    assert get_classification(9) == "EXCELLENT"

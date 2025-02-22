from utils.validations import validate_name, validate_grade

def test_validate_name():
    assert validate_name("Janira Huesca")
    assert not validate_name("Janira123")  # Nombres con números no deben ser válidos
    assert not validate_name("!Janira")  # Nombres con caracteres especiales no deben ser válidos

def test_validate_grade():
    assert validate_grade(8)  
    assert not validate_grade(11)  
    assert not validate_grade(-1)  
    assert not validate_grade("A")
    
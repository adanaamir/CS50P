from CS50P.ProblemSet_7.numb3rs import validate

def test_input():
    assert validate("1.2.3.4") == True
    assert validate("1.2.3") == False
    assert validate("1.2") == False
    assert validate("1") == False

def test_str():
    assert validate("cat") == False

def test_range():
    assert validate("255.255.255.255") == True
    assert validate("500.1.1.1") == False
    assert validate("1.500.1.1") == False
    assert validate("1.1.500.1") == False
    assert validate("1.1.1.500") == False
    

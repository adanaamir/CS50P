from ProblemSet_5.plates import is_valid

def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_length():
    assert is_valid("H") == False
    assert is_valid("ABCDEFGH") == False

def test_punc():
    assert is_valid("PI3.14") == False

def test_mid_num():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_firsttwo():
    assert is_valid("22") == False
    assert is_valid("A2") == False
    assert is_valid("AA") == True
    assert is_valid("A0") == False

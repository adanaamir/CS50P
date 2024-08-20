from CS50P.ProblemSet_7.um import count

def test_correct_string():
    assert count("um") == 1
    assert count("Um, hello?, um") == 2
    assert count("hello, there") == 0

def test_nested_string():
    assert count("yummy") == 0
    assert count("instrument") == 0

def test_case_sensitive():
    assert count("UM WHAT") == 1
    assert count("PLEASE UM TAKE THIS ALBUM") == 1
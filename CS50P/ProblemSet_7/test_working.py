from CS50P.ProblemSet_7.working import convert
import pytest

def test_correct_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    
def test_Incorrect_format():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_incorrect_hours_and_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("13 PM to 17PM")

        
import pytest
from ProblemSet_5.fuel import convert, gauge

def test_zeroerror():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_valueerror():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("2/1")

def test_full():
    assert convert("99/100") == 0.99 
    assert gauge(0.99) == "F"
    assert gauge(1) == "F"

def test_end():
    assert convert("0/4") == 0 
    assert gauge(0) == "E"

def test_frac():
    assert convert("1/4") == 0.25 
    assert gauge(0.25) == "25%"
    assert convert("50/100") == 0.5
    assert gauge(0.5) == "50%"

def test_invalid():
    with pytest.raises(ValueError):
        convert("1/2/3")
    with pytest.raises(ValueError):
        convert("1.5/2")

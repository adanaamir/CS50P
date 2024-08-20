from seasons import time
from datetime import date
import pytest

def test_normal():
    today = date.today()
    bday = date.fromisoformat("1999-01-01")
    assert time(today, bday) == 13466880

def test_invalid_format():
    with pytest.raises(ValueError):
        date.fromisoformat("January 1, 1999")

    with pytest.raises(ValueError):
        date.fromisoformat("cat")

    with pytest.raises(ValueError):
        date.fromisoformat("2023-10-99")

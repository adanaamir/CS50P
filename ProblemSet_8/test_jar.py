from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2

    jar.deposit(6)
    assert jar.size == 8

    with pytest.raises(ValueError):
        jar.deposit(7)

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(3)

def test_size():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(2)
    assert jar.size == 3
    assert jar.capacity == 12

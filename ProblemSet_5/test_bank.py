from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_h():
    assert value("hey") == 20
    assert value("Hi") == 20

def test_not_h():
    assert value("whats up") == 100
    assert value("Wassup") == 100

    
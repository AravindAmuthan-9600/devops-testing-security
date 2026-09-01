from app import add, subtract

def test_add():
    assert add(10, 20) == 30

def test_subtract():
    assert subtract(20, 10) == 10

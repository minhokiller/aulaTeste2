from app.calc import soma, subtrai, multiplica, divide

def test_soma():
    assert soma(2,3) == 5

def test_subtrai():
    assert subtrai(8,5) == 3

def test_multiplica():
    assert multiplica(2,5) == 10

def test_divide():
    assert divide(10,2) == 5
    try:
        divide(10,0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
    else:
        assert False, "Expected ValueError not raised"
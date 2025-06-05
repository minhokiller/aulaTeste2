from app.calc import soma, subtrai, multiplica

def test_soma():
    assert soma(2,3) == 5

def test_subtrai():
    assert subtrai(8,5) == 3

def test_multiplica():
    assert multiplica(2,5) == 10
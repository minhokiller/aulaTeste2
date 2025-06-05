from app.calc import soma, subtrai

def test_soma():
    assert soma(2,3) == 5

def test_subtrai():
    assert subtrai(8,5) == 3
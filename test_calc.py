import calc

def test_add():
    assert calc.add(2, 3) == 5

def test_div():
    assert calc.div(10, 2) == 5

def test_div_by_zero():
    try:
        calc.div(10, 0)
        assert False  # 예외 안 나면 실패
    except ValueError:
        assert True


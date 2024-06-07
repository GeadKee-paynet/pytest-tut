import pytest


def testOnePlusOne():
    assert 1 + 1 == 2

def testOnePlusTwo():
    a = 1
    b = 2
    c = 3
    assert a + b == c

def divideByZero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value) 



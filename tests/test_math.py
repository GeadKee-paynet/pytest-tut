import pytest


def testOnePlusOne():
    assert 1 + 1 == 2

def testOnePlusTwo():
    a = 1
    b = 2
    c = 3
    assert a + b == c

def testDivideByZero():
  with pytest.raises(ZeroDivisionError) as e:
    num = 1 / 0

  assert "division by zero" in str(e.value) 

# def test_divide_by_zero():
#   with pytest.raises(ZeroDivisionError) as e:
#     num = 1 / 0
  
#   assert 'division by zero' in str(e.value)

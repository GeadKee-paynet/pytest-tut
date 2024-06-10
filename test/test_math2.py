import pytest

## pytest.mark,parametrize


products = [
  (2, 3, 5),            # postive integers
  (1, 99, 99),          # identity
  (0, 99, 0),           # zero
  (3, -4, -12),         # positive by negative
  (-5, -5, 25),         # negative by negative
  (2.5, 6.7, 16.75)     # floats
]

@pytest.mark.parametrize("a, b, product", products)
def test_multiplication(a, b, product):
    assert a * b == product


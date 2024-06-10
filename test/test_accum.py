import pytest
from stuffs.accum import Accumulator

# accum = Accumulator()

def testAccumulatorInit():
    accum = Accumulator()
    assert accum.count == 0

def test_accumulator_init():
  accum = Accumulator()
  assert accum.count == 0


def test_accumulatorAdd():
    accum = Accumulator()
    accum.add()

    assert accum.count > 0

def test_accumulatorAddThree():
    accum = Accumulator()
    accum.add(3)

    assert accum.count == 3

def test_accumulatorAddTwice():
    accum = Accumulator()
    accum.add()
    accum.add()

    assert accum.count == 2

def test_accumulatorCannotSetCountDirectly():
    accum = Accumulator()
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter") as e:
        accum.count = 10

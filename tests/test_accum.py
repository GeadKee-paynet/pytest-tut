import pytest
from stuff.accum import Accumulator

## TO RUN SPECIFIC FUNCTION FROM A MODULE, 
## IN TERMINAL, "pytest the/path/to/file.py::function_name"


# Fixtures
# --------------------------------------------------------------------------------
@pytest.fixture
def accum():
  return Accumulator()

@pytest.mark.accumulator
def testAccumulatorInit(accum):
    assert accum.count == 0

@pytest.mark.accumulator
def test_accumulatorAdd(accum):
    accum.add()

    assert accum.count > 0

@pytest.mark.accumulator
def test_accumulatorAddThree(accum):
    accum.add(3)

    assert accum.count == 3

@pytest.mark.accumulator
def test_accumulatorAddTwice(accum):
    accum.add()
    accum.add()

    assert accum.count == 2

@pytest.mark.accumulator
def test_accumulatorCannotSetCountDirectly(accum):
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter") as e:
        accum.count = 10

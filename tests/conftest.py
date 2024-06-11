
## PYTEST WILL FIND ALL FIXTURES IN THIS FILE - "conftest.py"

import pytest
from stuffs.accum import Accumulator

@pytest.fixture
def accum():
    ##    yield is a generator
    yield Accumulator()
    ## whenever there's yield in a function, 
    ## then everything before this function the SETUP steps
    ## everything after is the CLEAN steps

    print("Done with the test!")

@pytest.fixture
def accum2():
    return Accumulator()
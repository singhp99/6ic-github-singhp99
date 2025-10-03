# Tests from https://www.softwaretestinghelp.com/pytest-tutorial/
import pytest
from example_functions import *

@pytest.mark.parametrize("a,b,c,tot", [(2, 2, 2,6), (3,4, 4, 11), (3, -2, 3, 4)])
def test_adder(a, b, c,tot):
    output = my_adder(a, b, c)
    assert output == tot
    
@pytest.mark.parametrize("temp,desired_temp,satus", [(28,22, "AC"), (10,21,"Heat"), (24, 24,"off")])
def test_temp(temp,desired_temp,satus):
    output = my_thermo_stat(temp,desired_temp)
    assert output == satus


@pytest.mark.parametrize("s,is_digit", [("abc",0), ("123",1), ("1.23", 1)])
def test_is_digit(s,is_digit):
    output = have_digits(s)
    assert output == is_digit



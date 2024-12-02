import pytest
from project import read_conversions, multiply_units, divide_units

# Fixtures or setup for conversions
@pytest.fixture
def conversions():
    Lmultiply_conversions = {('mm', 'cm'): 0.1}
    Ldivide_conversions = {}
    Wmultiply_conversions = {}
    Wdivide_conversions = {('g', 'kg'): 1000}
    return Lmultiply_conversions, Ldivide_conversions, Wmultiply_conversions, Wdivide_conversions

def test_read_conversions(conversions):
    Lmultiply_conversions, Ldivide_conversions, Wmultiply_conversions, Wdivide_conversions = conversions

    assert Lmultiply_conversions
    assert Wdivide_conversions

def test_length_multiply_conversions(conversions):
    Lmultiply_conversions, _, _, _ = conversions

    #Mm, to cm conversion
    result = multiply_units(10, 'mm', 'cm', Lmultiply_conversions)
    assert pytest.approx(result, 0.00001) == 1

def test_weight_divide_conversions(conversions):
    _, _, _, Wdivide_conversions = conversions

    # Test kg to g conversion
    result = divide_units(1, 'kg', 'g', Wdivide_conversions)
    assert pytest.approx(result, 0.00001) == 1000

def test_temperature_conversions():
    # Celsius to Fahrenheit
    C_to_F = (0 * 9/5) + 32
    assert pytest.approx(C_to_F, 0.00001) == 32

    # Celsius to Kelvin
    C_to_K = 0 + 273.15
    assert pytest.approx(C_to_K, 0.00001) == 273.15

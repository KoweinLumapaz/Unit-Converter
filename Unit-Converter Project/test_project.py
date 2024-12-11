import pytest
import tkinter as tk
from project import multiply_units, divide_units, UnitConverterApp

# Example conversion data for testing
Lmultiply_conversions = {('cm', 'mm'): 10}
Ldivide_conversions = {('mm', 'm'): 1000}

Wmultiply_conversions = {('g', 'kg'): 1000}
Wdivide_conversions = {('kg', 'g'): 1000}

currency_rates = {'PHP': 1, 'EUR': 0.016, 'USD': 0.017, 'JPY': 2.62}

def test_multiply_units():
    assert multiply_units(100, 'cm', 'mm', Lmultiply_conversions) == 1000.0

def test_divide_units():
    assert divide_units(1, 'mm', 'm', Ldivide_conversions) == 0.001

def test_convert_length():
    root = tk.Tk()
    converter = UnitConverterApp(root)
    converter.Lmultiply_conversions = Lmultiply_conversions
    converter.Ldivide_conversions = Ldivide_conversions
    assert converter.convert_length(100, 'cm', 'mm') == 1000

def test_convert_weight():
    root = tk.Tk()
    converter = UnitConverterApp(root)
    converter.Wmultiply_conversions = Wmultiply_conversions
    converter.Wdivide_conversions = Wdivide_conversions
    assert converter.convert_weight(100, 'kg', 'g') == 0.1

def test_convert_temperature():
    root = tk.Tk()
    app = UnitConverterApp(root)
    assert app.convert_temperature(0, 'C', 'F') == 32.0
    assert app.convert_temperature(32, 'F', 'C') == 0.0
    assert app.convert_temperature(0, 'C', 'K') == 273.15

def test_convert_currency():
    root = tk.Tk()
    app = UnitConverterApp(root)
    app.currency_rates = currency_rates
    assert round(app.convert_currency(1, 'USD', 'PHP')) == 59
    assert round(app.convert_currency(50, 'PHP', 'USD')) == 1
    assert round(app.convert_currency(10, 'EUR', 'JPY')) == 1638

if __name__ == "__main__":
    pytest.main()

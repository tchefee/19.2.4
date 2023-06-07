import pytest

from app.calc import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator()

    def test_adding(self):
        assert self.calc.adding(2,2) == 4

    def test_subtraction(self):
        assert self.calc.subtraction(5, 2) == 3

    def test_multiply(self):
        assert self.calc.multiply(4, 3) == 12

    def test_division(self):
        assert self.calc.division(10,2) == 5
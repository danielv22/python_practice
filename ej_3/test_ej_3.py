from ej_3.main import getMinumumAmountOfChange
import unittest

class TestGetMinumumAmountOfChange(unittest.TestCase):
    def test_coins_1(self):
        input = [5, 7, 1, 1, 2, 3, 22]
        value_expected = 20
        response = getMinumumAmountOfChange(input)

        self.assertEqual(response, value_expected)

    def test_coins_2(self):
        input = [1, 1, 1, 1, 1]
        value_expected = 6
        response = getMinumumAmountOfChange(input)

        self.assertEqual(response, value_expected)

    def test_coins_3(self):
        input = [1, 5, 1, 1, 1, 10, 15, 20, 100]
        value_expected = 55
        response = getMinumumAmountOfChange(input)

        self.assertEqual(response, value_expected)
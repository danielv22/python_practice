from ej_2.main import squareNumbers
import unittest

class TestLookForNAndDele(unittest.TestCase):
    __s = 8

    def test_big_numbers(self):
        input = [120, 99, 1, 25, 2, 18]
        value_expected = [1, 4]
        response = squareNumbers(input, self.__s)

        self.assertEqual(response, value_expected)

    def test_empty_list(self):
        input = []
        value_expected = []
        response = squareNumbers(input, self.__s)

        self.assertEqual(response, value_expected)

    def test_invalid_list(self):
        input = ["120d", "a99", "1y", 2, 25, 18]
        value_expected = "La lista debe contener solo valores numéricos."

        with self.assertRaises(ValueError) as error:
            squareNumbers(input, self.__s)

        self.assertEqual(str(error.exception), value_expected)

    def test_numbers_as_str(self):
        input = ["120", "99", "1", "2", "25", "19"]
        value_expected = [1, 4]

        response = squareNumbers(input, self.__s)

        self.assertEqual(response, value_expected)

    def test_s_invalid(self):
        input = [0, 9, 1, 4, 2]
        s = 10
        value_expected = 'El valor de "s" debe estar entre 0 y 9'

        with self.assertRaises(ValueError) as error:
            squareNumbers(input, s)

        self.assertEqual(str(error.exception), value_expected)
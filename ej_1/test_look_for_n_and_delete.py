from ej_1.main import lookForNAndDelete
import unittest


class TestLookForNAndDelete(unittest.TestCase):
    __s = 8

    def test_empty_array(self):
        input = []
        response_expected = []
        response = lookForNAndDelete(input, self.__s)

        self.assertEqual(response, response_expected)

    def test_remove_simgle_digit(self):
        input = [120, 99, 1, 2, 25, 18]
        response_expected = [1, 1, 2, 25, 99, 120]
        response = lookForNAndDelete(input, self.__s)

        self.assertEqual(response, response_expected)

    def test_letters_in_array(self):
        input = ["120d", "a99", "1y", 2, 25, 18]
        response_expected = "La lista debe contener solo valores numéricos."

        with self.assertRaises(ValueError) as error:
            lookForNAndDelete(input, self.__s)

        self.assertEqual(str(error.exception), response_expected)

    def test_numbers_as_str(self):
        input = ["120", "99", "1", "2", "25", "19"]
        response_expected = [1, 2, 19, 25, 99, 120]
        response = lookForNAndDelete(input, self.__s)

        self.assertEqual(response, response_expected)

    def test_withot_occurrences(self):
        input = [120, 99, 1, 2, 25, 19]
        response_expected = [1, 2, 19, 25, 99, 120]
        response = lookForNAndDelete(input, self.__s)

        self.assertEqual(response, response_expected)

    def test_multiple_occurreceness_same_number(self):
        input = [1, 10, 88, 888]
        response_expected = [1, 10]
        response = lookForNAndDelete(input, self.__s)

        self.assertEqual(response, response_expected)

if __name__ == "__main__":
    unittest.main()
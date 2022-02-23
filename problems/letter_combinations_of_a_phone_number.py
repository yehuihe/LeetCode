import unittest
from itertools import product


PHONE_DIGITS = {
    2: ("a", "b", "c"),
    3: ("d", "e", "f"),
    4: ("g", "h", "i"),
    5: ("j", "k", "l"),
    6: ("m", "n", "o"),
    7: ("p", "q", "r", "s"),
    8: ("t", "u", "v"),
    9: ("w", "x", "y", "z"),
}


def letterCombinations(digits: str) -> list:
    # empty digits case
    if digits == "":
        return []

    mapping = [PHONE_DIGITS[int(digit)] for digit in digits]
    return ["".join(v) for v in list(product(*tuple(mapping)))]


class TestLetterCombinations(unittest.TestCase):
    def test_1(self):
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(letterCombinations(digits), expected)

    def test_2(self):
        digits = ""
        expected = []
        self.assertEqual(letterCombinations(digits), expected)

    def test_3(self):
        digits = "2"
        expected = ["a", "b", "c"]
        self.assertEqual(letterCombinations(digits), expected)


if __name__ == "__main__":
    unittest.main()

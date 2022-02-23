import unittest


ROMAN_NUMERALS = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}


def intToRoman(num: int) -> str:
    """
    Constraints 1 <= num <= 3999
    """
    result = []
    for k, v in ROMAN_NUMERALS.items():
        quotient, remainder = divmod(num, k)
        result.append(v * quotient)
        if remainder == 0:
            break
        num = remainder

    return "".join(result)


class TestIntToRoman(unittest.TestCase):

    def test_1(self):
        num = 3
        self.assertEqual(intToRoman(num), "III")

    def test_2(self):
        num = 58
        self.assertEqual(intToRoman(num), "LVIII")

    def test_3(self):
        num = 1994
        self.assertEqual(intToRoman(num), "MCMXCIV")


if __name__ == "__main__":
    unittest.main()

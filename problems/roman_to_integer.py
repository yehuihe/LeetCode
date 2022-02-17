ROMAN_NUMERALS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def romanToInt(s: str) -> int:
    res = 0

    i = 0
    while i < len(s) - 1:
        if ROMAN_NUMERALS[s[i]] < ROMAN_NUMERALS[s[i + 1]]:
            res += ROMAN_NUMERALS[s[i + 1]] - ROMAN_NUMERALS[s[i]]
            i += 2
        else:
            res += ROMAN_NUMERALS[s[i]]
            i += 1

    if i != len(s):
        res += ROMAN_NUMERALS[s[-1]]

    return res


def main():
    # s = "III"
    # s = "LVIII"
    s = "MCMXCIV"
    print(romanToInt(s))


if __name__ == "__main__":
    main()

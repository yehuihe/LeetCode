def convert_to_32_bit_int(num: int) -> int:
    if num < -(2**31):
        return -(2**31)
    if num >= 2**31 - 1:
        return 2**31 - 1
    return num


def myAtoi(s: str) -> int:
    s = s.strip()

    # empty s case. s = ""
    if s == "":
        return 0

    # initial "+", "-" sign
    negative = False
    if s[0] == "+":
        s = s[1:]
    elif s[0] == "-":
        negative = True
        s = s[1:]

    temp = ""
    for c in s:
        if not c.isdigit():
            break
        temp += c

    if negative:
        temp_int = -int(temp) if temp != "" else 0
    else:
        temp_int = int(temp) if temp != "" else 0

    return convert_to_32_bit_int(temp_int)


def main():
    # s = "42"
    # s = "   -42"
    # s = "4193 with words"
    # s = "words and 987"
    # s = "+1"
    s = "+-12"
    print(myAtoi(s))


if __name__ == "__main__":
    main()

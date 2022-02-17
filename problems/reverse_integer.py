def is_signed_32_bit_int(num: int) -> bool:
    return True if -(2**31) <= num <= 2**31 - 1 else False


def reverse(x: int) -> int:
    """Given a signed 32-bit integer x, return x with its digits reversed.
     If reversing x causes the value to go outside the signed 32-bit
     integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers
     (signed or unsigned).
    """
    x_str = str(x)
    if x_str[0] == "-":
        num = -int(x_str[:0:-1])
        return num if is_signed_32_bit_int(num) else 0
    num = int(x_str[::-1])
    return num if is_signed_32_bit_int(num) else 0


def main():
    # x = 123
    # x = -123
    # x = 120
    x = 1534236469
    print(reverse(x))


if __name__ == "__main__":
    main()

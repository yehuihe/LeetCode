def isPalindrome(x: int) -> bool:
    x_str = str(x)
    for i in range(len(x_str) // 2):
        if x_str[i] != x_str[len(x_str) - i - 1]:
            return False
    return True


def main():
    # x = 123
    # x = -123
    x = 10
    print(isPalindrome(x))


if __name__ == "__main__":
    main()

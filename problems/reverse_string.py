def reverseStringLinear(s: list) -> None:
    """Linear solution
    Do not return anything, modify s in-place instead.
    O(1) space complexity
    """
    for i in range(len(s) // 2):
        s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
    return


def reverseStringTwoPoint(s: list) -> None:
    """Two pointer solution
    Do not return anything, modify s in-place instead.
    O(1) space complexity
    """
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return


def main():
    # s = ["h","e","l","l","o"]
    s = ["H","a","n","n","a","h"]
    # print(reverseStringLinear(s))
    print(reverseStringTwoPoint(s))
    print(s)


if __name__ == "__main__":
    main()



def isPalindrome(word: str) -> bool:
    return word == word[::-1]


def longestPalindromeBrute(s: str) -> str:
    """Given a string s, return the longest palindromic substring in s.

    O(n^3) brute-force solution
    """
    # Single character case. i.e. s = "a"
    if len(s) == 1:
        return s

    palindrom = None
    max_len = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if isPalindrome(s[i:j]) and (j - i > max_len):
                palindrom = s[i:j]
                max_len = j - i
    return palindrom


def longestPalindromeDP(s: str) -> str:
    """Given a string s, return the longest palindromic substring in s.

    O(n^2) dynamic programming solution
    """
    # Single character case. i.e. s = "a"
    if len(s) == 1:
        return s

    palindrom = None
    max_len = 0

    dp = [[False] * len(s) for _ in range(len(s))]
    for i in reversed(range(len(s))):
        dp[i][i] = True
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                if j - i == 1 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if max_len < j - i + 1:
                        max_len = j - i + 1
                        palindrom = s[i : j + 1]
    return palindrom


def main():
    s = "babad"
    # s = "cbbd"
    # s = "a"
    # s = "bb"
    # s = "jkexvzsqshsxyytjmmhauoyrbxlgvdovlhzivkeixnoboqlfemfzytbolixqzwkfvnpacemgpotjtqokrqtnwjpjdiidduxdprngvitnzgyjgreyjmijmfbwsowbxtqkfeasjnujnrzlxmlcmmbdbgryknraasfgusapjcootlklirtilujjbatpazeihmhaprdxoucjkynqxbggruleopvdrukicpuleumbrgofpsmwopvhdbkkfncnvqamttwyvezqzswmwyhsontvioaakowannmgwjwpehcbtlzmntbmbkkxsrtzvfeggkzisxqkzmwjtbfjjxndmsjpdgimpznzojwfivgjdymtffmwtvzzkmeclquqnzngazmcfvbqfyudpyxlbvbcgyyweaakchxggflbgjplcftssmkssfinffnifsskmsstfclpjgblfggxhckaaewyygcbvblxypduyfqbvfcmzagnznquqlcemkzzvtwmfftmydjgvifwjoznzpmigdpjsmdnxjjfbtjwmzkqxsizkggefvztrsxkkbmbtnmzltbchepwjwgmnnawokaaoivtnoshywmwszqzevywttmaqvncnfkkbdhvpowmspfogrbmuelupcikurdvpoelurggbxqnykjcuoxdrpahmhiezaptabjjulitrilkltoocjpasugfsaarnkyrgbdbmmclmxlzrnjunjsaefkqtxbwoswbfmjimjyergjygzntivgnrpdxuddiidjpjwntqrkoqtjtopgmecapnvfkwzqxilobtyzfmeflqobonxiekvizhlvodvglxbryouahmmjtyyxshsqszvxekj"
    # s = "ac"
    print(longestPalindromeDP(s))


if __name__ == "__main__":
    main()

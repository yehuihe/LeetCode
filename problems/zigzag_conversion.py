# TODO:
def convert(s: str, numRows: int) -> str:
    """The string "PAYPALISHIRING" is written in a zigzag pattern on a given
     number of rows like this: (you may want to display this pattern in
     a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R

    And then read line by line: "PAHNAPLSIIGYIR"
    """
    zigzag = [[]] * numRows
    temp = []
    i = 0
    col = 0
    rows = []
    # for i in s:




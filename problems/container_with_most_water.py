def maxAreaBrute(height: list) -> int:
    """O(n^2) time complexity brute-force solution"""
    max_amount = 0
    for i in range(len(height) - 1):
        for j in range(i + 1, len(height)):
            area = (j - i) * min(height[i], height[j])
            if max_amount < area:
                max_amount = area
    return max_amount


def maxAreaTwoPointer(height: list) -> int:
    """O(n) time complexity two pointer solution

    O(1) in-place space complexity
    """
    max_amount = 0

    i, j = 0, len(height) - 1
    while i < j:
        area = (j - i) * min(height[i], height[j])
        if max_amount < area:
            max_amount = area
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_amount


def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # height = [1, 1]
    print(maxAreaTwoPointer(height))


if __name__ == "__main__":
    main()

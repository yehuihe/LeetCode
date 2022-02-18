def removeDuplicates(nums: list) -> int:
    """Two pointer techniques

    O(n) time complexity, O(1) space complexity
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


def main():
    # nums = [1, 1, 2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(removeDuplicates(nums))


if __name__ == "__main__":
    main()

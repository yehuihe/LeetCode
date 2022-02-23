from collections import Counter
import unittest


def remove_duplicates(lst: list) -> list:
    duplicates = []
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if Counter(lst[i]) == Counter(lst[j]):
                duplicates.append(lst[j])
    for duplicate in duplicates:
        lst.remove(duplicate)
    return lst


def threeSumBrute(nums: list) -> list:
    """O(n^3) solution"""
    # nums has less than three elements case
    if len(nums) in (0, 1, 2):
        return []

    res = []

    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])

    return remove_duplicates(res)


# TODO: Still wrong
def threeSumTwoPointer(nums: list) -> list:
    # nums has less than three elements case
    if len(nums) < 3:
        return []

    res = []

    nums = sorted(nums)
    for i in range(len(nums) - 2):
        if nums[i] != nums[i+1]:
            low, high = i+1, len(nums) - 1
            sum = -nums[i]

            while low < high:
                if nums[low] + nums[high] == sum:
                    res.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] < sum:
                    low += 1
                else:
                    high -= 1
    return res


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = []
    # nums = [0]
    # nums = [0, 0, 0, 0]
    print(threeSumTwoPointer(nums))


if __name__ == '__main__':
    main()

import math
import unittest


def threeSumClosestBrute(nums: list, target: int) -> int:
    """O(n^3) time complexity two pointer solution

    O(n) in-place space complexity
    """

    res = []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                res.append(nums[i] + nums[j] + nums[k])

    distance = [abs(v - target) for v in res]
    min_distance = min(distance)
    return res[distance.index(min_distance)]


def threeSumClosestTwoPointer(nums: list, target: int) -> int:
    """O(n^2) time complexity two pointer solution

    O(1) in-place space complexity
    """
    nums = sorted(nums)

    res = 0

    min_sum = math.inf
    for i in range(len(nums) - 2):
        low, high = i + 1, len(nums) - 1
        while low < high:
            three_sum = nums[i] + nums[low] + nums[high]
            if three_sum == target:
                return target
            elif three_sum < target:
                low += 1
            else:
                high -= 1
            if abs(three_sum - target) < min_sum:
                min_sum = abs(three_sum - target)
                res = three_sum
    return res


class TestThreeSumClosestTwoPointer(unittest.TestCase):
    def test_1(self):
        nums = [-1, 2, 1, -4]
        target = 1
        self.assertEqual(threeSumClosestTwoPointer(nums, target), 75)

    def test_2(self):
        nums = [0, 0, 0]
        target = 1
        self.assertEqual(threeSumClosestTwoPointer(nums, target), 0)

    def test_3(self):
        nums = [1, 1, 1, 1]
        target = 3
        self.assertEqual(threeSumClosestTwoPointer(nums, target), 3)


if __name__ == "__main__":
    unittest.main()

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if i == j:
                    continue

                if n + m == target:
                    return [i, j]

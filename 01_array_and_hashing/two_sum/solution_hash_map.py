class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map: dict[int, int] = {}

        for i, n in enumerate(nums):
            if target - n in hash_map:
                return [i, hash_map[target - n]]
            hash_map[n] = i

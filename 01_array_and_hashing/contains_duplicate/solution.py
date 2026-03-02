class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_map: dict[int, int] = {}

        for i, num in enumerate(nums):
            if num in hash_map:
                return True

            hash_map[num] = i
        return False

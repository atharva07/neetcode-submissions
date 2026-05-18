class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for item in nums:
            freq[item] = freq.get(item, 0) + 1

        for key, value in freq.items():
            if value > 1:
                return True

        return False
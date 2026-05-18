class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for item in nums:
            freq[item] = freq.get(item, 0) + 1

        sorted_freq = sorted(freq.items(), key = lambda x: x[1], reverse=True)
        res = []

        for i in range(k):
            res.append(sorted_freq[i][0])

        return res

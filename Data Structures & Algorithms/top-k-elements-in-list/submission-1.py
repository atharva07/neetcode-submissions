class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # Store the frequency of each item in a dict
        for item in nums:
            freq[item] = freq.get(item, 0) + 1

        # sort the freq dict based on the value using lamba functions
        sorted_freq = sorted(freq.items(), key = lambda x: x[1], reverse=True)
        res = []

        # Traverse the frequency till k and store the key in result
        for i in range(k):
            res.append(sorted_freq[i][0])

        # return result
        return res
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = Counter(nums)
        most_frequent = numbers.most_common(k)

        final = [num for num, count in most_frequent]

        return final
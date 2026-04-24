class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [val for val, freq in heapq.nlargest(k, count.items(), key = lambda x : x[1])]
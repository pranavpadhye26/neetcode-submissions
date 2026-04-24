class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = 0
        freq = Counter(tasks)
        maxFreq = max(freq.values())
        
        maxFreqCount = sum(1 for freq in freq.values() if freq == maxFreq)

        return max(len(tasks), (maxFreq - 1) * (n + 1) + maxFreqCount)
        
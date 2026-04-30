class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            large1 = -heapq.heappop(stones)
            large2 = -heapq.heappop(stones)

            if large1 == large2:
                continue
            if large1 > large2:
                res = abs(large1 - large2)
            heapq.heappush(stones,-res)

        return -stones[0] if stones else 0
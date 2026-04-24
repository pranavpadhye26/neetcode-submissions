class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            largest1 = -heapq.heappop(stones)
            largest2 = -heapq.heappop(stones)

            if largest1 == largest2:
                continue
            if largest1 > largest2:
                value = abs(largest1 - largest2)
                heapq.heappush(stones , -value)

        return -stones[0] if stones else 0   
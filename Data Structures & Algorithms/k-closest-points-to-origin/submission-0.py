class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x2,y2 in points:
            dist = (x2 - 0)**2 + (y2 - 0)**2
            heap.append((dist,x2,y2))

        heapq.heapify(heap)
        result = []
        for i in range(k):
            dist, x, y= heapq.heappop(heap)
            result.append([x,y])
        return result


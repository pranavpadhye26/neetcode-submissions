class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        for x1,y1 in points:
            dist = (x1**2) + (y1**2)
            heapq.heappush(heap,(dist, x1, y1))

        for i in range(k):
            dist, x , y = heapq.heappop(heap)
            res.append([x,y])

        return res
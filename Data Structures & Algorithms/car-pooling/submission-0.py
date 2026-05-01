class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        heap = []
        passengers = 0
        for people,start,end in trips:
            while heap and heap[0][0] <= start:
                currEnd, off = heapq.heappop(heap)
                passengers -= off
            passengers += people
            heapq.heappush(heap,(end,people))
            if passengers > capacity:
                return False
        return True
        
        

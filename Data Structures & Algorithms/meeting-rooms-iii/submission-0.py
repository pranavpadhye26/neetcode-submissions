class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        busy = []
        available = []
        for i in range(n):
            available.append(i)
        
        count = [0] * n

        for start,end in sorted(meetings):
            while busy and busy[0][0] <= start:
                _ , room = heapq.heappop(busy)
                heapq.heappush(available,room)
            
            if not available:
                end_time, room = heapq.heappop(busy)
                end = end_time + (end - start)
                heapq.heappush(available,room)
            
            room = heapq.heappop(available)
            heapq.heappush(busy,(end,room))
            count[room] += 1
        
        return count.index(max(count))

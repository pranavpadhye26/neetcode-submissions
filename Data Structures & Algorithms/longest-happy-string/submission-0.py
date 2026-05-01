class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        freq = {'a': a, 'b': b, 'c': c}
        heap = []

        for ch, count in freq.items():
            if count > 0:
                heapq.heappush(heap, (-count, ch))
        
        while heap:
            count, ch = heapq.heappop(heap)
            count = - count
            if len(res) >= 2 and res[-1] == res[-2] == ch:
                if not heap:
                    break
                count2, ch2 = heapq.heappop(heap)
                heapq.heappush(heap,(-count,ch))
                count2 = - count2
                res += ch2
                count2 -= 1
                if count2 > 0:
                    heapq.heappush(heap,(-count2,ch2))
            else:
                res += ch
                count -= 1
                if count > 0:
                    heapq.heappush(heap,(-count,ch))
    
        return res
